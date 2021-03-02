from django.contrib import admin

from company.models import Worker, Child, Task
from realty.models import Client


class TaskInline(admin.TabularInline):
    model = Task
    fields = ('text', 'worker', 'priority', 'status', 'date_start', 'date_end',)
    extra = 0


class ChildInline(admin.TabularInline):
    model = Child
    fields = ('name', 'date_of_birthday', 'sex')
    extra = 0


class ClientInline(admin.TabularInline):
    model = Client
    fields = ('fio', 'phone', 'email', 'date_of_birthday', 'comment')
    extra = 0


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'date_of_birthday')
    search_fields = ('fio', 'phone')
    inlines = (ClientInline, ChildInline)
