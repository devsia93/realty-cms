from django.contrib import admin

from realty.models import Realty


@admin.register(Realty)
class RealtyAdmin(admin.ModelAdmin):
    list_display = ('address',
                    'price',
                    'get_floor',
                    'count_rooms',
                    'square',
                    'type_material',
                    'type_layout',
                    'type_realty',
                    'type_deal',
                    'status',
                    'owner',
                    'comment')
    search_fields = ('owner__fio',
                     'owner__email',
                     'owner__phone',
                     'address',
                     'comment')
    list_filter = ('status',)

    def get_floor(self, obj):
        return f'{obj.floor}/{obj.floors}'

    get_floor.short_description = 'Этаж'
