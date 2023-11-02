from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='E-mail')
    name = models.CharField(max_length=250, verbose_name='ФИО')
    avatar = models.ImageField(upload_to='static/media/avatars', **NULLABLE, verbose_name='Аватар')
    phone = models.IntegerField(**NULLABLE, verbose_name='Телефон')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
