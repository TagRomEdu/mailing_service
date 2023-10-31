from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='E-mail')
    name = models.CharField(max_length=250, verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

