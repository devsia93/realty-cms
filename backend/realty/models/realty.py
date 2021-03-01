from django.db import models

from realty.custom_decimal_field import CustomDecimalField
from realty.models.client import Client


class Realty(models.Model):
    class TYPE_DEAL:
        UNKNOWN = 0
        SALE = 1
        RENT = 2

        CHOICES = (
            (UNKNOWN, 'Не определено'),
            (SALE, 'Продажа'),
            (RENT, 'Аренда'),
        )

    address = models.CharField(max_length=128, verbose_name='Адрес')
    owner = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE, related_name='realties',
                              verbose_name='Владелец')
    type_deal = models.IntegerField(choices=TYPE_DEAL.CHOICES, default=TYPE_DEAL.UNKNOWN, blank=True,
                                    verbose_name='Статус')
    price = CustomDecimalField(verbose_name='Цена')


    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимости'

    def __str__(self):
        return self.address
