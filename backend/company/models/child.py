from django.db import models


class Child(models.Model):
    class SEX:
        FEMALE = 0
        MALE = 1

        CHOICES = (
            (FEMALE, 'Женский'),
            (MALE, 'Мужской'),
        )

    name = models.CharField(max_length=128, verbose_name='Имя')
    sex = models.IntegerField(choices=SEX.CHOICES, default=SEX.FEMALE, blank=True, null=True, verbose_name='Пол')
    date_of_birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

    def __str__(self):
        return self.name
