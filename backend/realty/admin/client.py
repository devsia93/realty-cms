from django.contrib import admin
from django.shortcuts import render

from realty.models import Client
from services.const import PHONES, ADMIN_MODEL_URL
from services.sms import SMS


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'email', 'date_of_birthday', 'comment')
    search_fields = ('fio', 'phone', 'email', 'comment')
    actions = ('send_sms',)

    def send_sms(self, request, queryset):
        request.session[PHONES] = [q.phone for q in queryset]
        request.session[ADMIN_MODEL_URL] = request.path

        return render(request, 'admin/send_sms.html', context={'admin_model_url': request.path})

    send_sms.short_description = 'Отправить СМС'
