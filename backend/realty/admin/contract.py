from django.contrib import admin

from realty.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    ...
