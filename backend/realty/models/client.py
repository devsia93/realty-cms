from django.db import models


class Client(models.Model):
    fio = models.CharField(max_length=128, verbose_name='ФИО')
    date_of_birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, null=True, verbose_name='Почта')
    comment = models.CharField(max_length=256, blank=True, null=True, verbose_name='Примечание')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.fio
