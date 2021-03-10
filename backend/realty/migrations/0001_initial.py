# Generated by Django 3.1.7 on 2021-03-10 13:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
import realty.custom_decimal_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=128, verbose_name='ФИО')),
                ('date_of_birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('comment', models.CharField(blank=True, max_length=256, null=True, verbose_name='Примечание')),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='company.worker', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='TypeLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Планировка',
                'verbose_name_plural': 'Планировки',
            },
        ),
        migrations.CreateModel(
            name='TypeMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип материала',
                'verbose_name_plural': 'Типы материалов',
            },
        ),
        migrations.CreateModel(
            name='TypePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип оплаты',
                'verbose_name_plural': 'Типы оплаты',
            },
        ),
        migrations.CreateModel(
            name='TypeRealty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип недвижимости',
                'verbose_name_plural': 'Типы недвижимости',
            },
        ),
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес')),
                ('price', realty.custom_decimal_field.CustomDecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Цена')),
                ('floor', models.IntegerField(blank=True, default=1, null=True, verbose_name='Этаж')),
                ('floors', models.IntegerField(blank=True, default=1, null=True, verbose_name='Этажность')),
                ('count_rooms', models.IntegerField(verbose_name='Кол-во комнат')),
                ('square', models.CharField(blank=True, max_length=64, null=True, verbose_name='Площадь (общая/жилая/кухня)')),
                ('type_deal', models.IntegerField(blank=True, choices=[(0, 'Не определено'), (1, 'Продажа'), (2, 'Аренда')], default=0, verbose_name='Тип сделки')),
                ('status', models.BooleanField(default=True, verbose_name='Активно?')),
                ('comment', models.CharField(blank=True, max_length=256, null=True, verbose_name='Примечание')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realties', to='realty.client', verbose_name='Владелец')),
                ('type_layout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='realties', to='realty.typelayout', verbose_name='Тип планировки')),
                ('type_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='realties', to='realty.typematerial', verbose_name='Тип материала')),
                ('type_realty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='realties', to='realty.typerealty', verbose_name='Тип недвижимости')),
            ],
            options={
                'verbose_name': 'Недвижимость',
                'verbose_name_plural': 'Недвижимости',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', realty.custom_decimal_field.CustomDecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Сумма')),
                ('amount_commission', realty.custom_decimal_field.CustomDecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Сумма комиссии')),
                ('date_of_deal', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Дата сделки')),
                ('agreement', models.FileField(upload_to='agreements', verbose_name='Договор')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to='realty.client', verbose_name='Клиент')),
                ('main_worker', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to='company.worker', verbose_name='Сотрудник #1')),
                ('realty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to='realty.realty', verbose_name='Недвижимость')),
                ('sub_worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_deals', to='company.worker', verbose_name='Сотрудник #2')),
                ('type_payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='realty.typepayment', verbose_name='Тип оплаты')),
            ],
            options={
                'verbose_name': 'Сделка',
                'verbose_name_plural': 'Сделки',
            },
        ),
    ]