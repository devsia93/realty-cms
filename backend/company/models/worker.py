from django.db import models


class Worker(models.Model):
    fio = models.CharField(max_length=128, verbose_name='ФИО')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, null=True, verbose_name='Адрес')
    date_of_birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.fio
