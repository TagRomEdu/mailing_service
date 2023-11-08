from django.contrib import admin

from mailing_app.models import Client, Mailing, Message, MailingLog, Blog
from users_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone', 'is_active')
    list_editable = ('is_active',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name',)
    list_search = ('name',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'period', 'status', 'user')
    list_filter = ('period', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'mailing', 'user')
    list_filter = ('subject', 'body')
    list_search = ('subject', 'body')


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('time', 'status', 'mailing', 'error_msg')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_published', 'user')