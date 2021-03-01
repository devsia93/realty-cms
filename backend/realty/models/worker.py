from django.db import models

from realty.models import Client
from realty.models.child import Child
from realty.models.deal import Deal
from realty.models.task import Task


class Worker(models.Model):
    fio = models.CharField(max_length=128, verbose_name='ФИО')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    date_of_birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    kids = models.ForeignKey(Child, blank=True, null=True, on_delete=models.CASCADE, related_name='worker',
                             verbose_name='Дети')
    clients = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL, related_name='worker',
                                verbose_name='Клиенты')
    deals = models.ForeignKey(Deal, blank=True, null=True, on_delete=models.SET_NULL, related_name='worker',
                              verbose_name='Сделки')
    tasks = models.ForeignKey(Task, blank=True, null=True, on_delete=models.CASCADE, related_name='worker',
                              verbose_name='Задачи')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.fio
