from django.contrib import admin

from realty.models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('worker', 'client', 'amount', 'amount_commission', 'type_payment', 'date_of_deal', 'agreement')
    search_fields = ('worker__fio', 'client__fio', 'worker__email', 'client__email', 'worker__phone', 'client__phone')
    list_filter = ('type_payment',)
