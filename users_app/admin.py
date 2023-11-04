from django.contrib import admin

from mailing_app.models import Client, Mailing, Message
from users_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)
    list_search = ('name',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'period', 'status')
    list_filter = ('period', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'mailing', 'user')
    list_filter = ('subject', 'body')
    list_search = ('subject', 'body')

