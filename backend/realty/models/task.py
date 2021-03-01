from django.db import models


class Task(models.Model):
    class PRIORITY:
        LOW = 0
        MIDDLE = 1
        HIGH = 2

        CHOICES = (
            (LOW, 'Низкий'),
            (MIDDLE, 'Средний'),
            (HIGH, 'Высокий'),
        )
    text = models.TextField(verbose_name='Текст')
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания')
    priority = models.IntegerField(choices=PRIORITY.CHOICES, default=PRIORITY.MIDDLE, verbose_name='Приоритет')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

