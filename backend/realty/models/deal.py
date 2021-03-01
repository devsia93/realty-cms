from django.db import models
from datetime import date

from company.models import Worker
from realty.custom_decimal_field import CustomDecimalField
from realty.models.client import Client
from realty.models.type_payment import TypePayment


class Deal(models.Model):
    worker = models.ForeignKey(Worker, null=True, on_delete=models.SET_NULL, related_name='deals',
                               verbose_name='Сотрудник')
    amount = CustomDecimalField(verbose_name='Сумма')
    amount_commission = CustomDecimalField(verbose_name='Сумма комиссии')
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL, related_name='deals',
                               verbose_name='Клиент')
    date_of_deal = models.DateField(verbose_name='Дата сделки', blank=True, null=True, default=date.today)
    agreement = models.FileField(upload_to='agreements', verbose_name='Договор')
    type_payment = models.ForeignKey(TypePayment, on_delete=models.PROTECT, verbose_name='Тип оплаты')

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):
        return f'Сделка #{self.id}'
