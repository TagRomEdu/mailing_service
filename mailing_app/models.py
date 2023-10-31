from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='E-mail')
    name = models.CharField(max_length=250, verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневно'),
        (PERIOD_WEEKLY, 'Еженедельно'),
        (PERIOD_MONTHLY, 'Ежемесячно')
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_COMPLETED = 'completed'

    STATUSES = (
        (STATUS_CREATED, 'создана'),
        (STATUS_CREATED, 'запущена'),
        (STATUS_CREATED, 'завершена'),
    )

    mailing_time = models.TimeField
    period = models.CharField(max_length=50, choices=PERIODS)
    status = models.CharField(max_length=50, choices=STATUSES)
    message = models.ForeignKey(Message, on_delete='SET_NULL')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingLog(models.Model):
    pass