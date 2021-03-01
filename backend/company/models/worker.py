from django.db import models

from realty.models import Client
from company.models.child import Child


class Worker(models.Model):
    fio = models.CharField(max_length=128, verbose_name='ФИО')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    date_of_birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    kids = models.ForeignKey(Child, blank=True, null=True, on_delete=models.CASCADE, related_name='worker',
                             verbose_name='Дети')
    clients = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL, related_name='worker',
                                verbose_name='Клиенты')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.fio
