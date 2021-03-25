from django.contrib import admin
from django.shortcuts import render

from realty.models import Client
from services.const import PHONES, ADMIN_MODEL_URL, PRICE_SMS
from services.sms import SMSService


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'email', 'date_of_birthday', 'comment')
    search_fields = ('fio', 'phone', 'email', 'comment')
    actions = ('send_sms',)

    def send_sms(self, request, queryset):
        phones = [q.phone for q in queryset]
        count_phones = len(phones)
        balance = SMSService().get_current_balance()
        price = count_phones * PRICE_SMS
        request.session[PHONES] = phones
        request.session[ADMIN_MODEL_URL] = request.path

        context = {
            'admin_model_url': request.path,
            'balance': balance,
            'count_phones': count_phones,
            'price': price
        }
        return render(request, 'admin/send_sms.html', context=context)

    send_sms.short_description = 'Отправить СМС'
