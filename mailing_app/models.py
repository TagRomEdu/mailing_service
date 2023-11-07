from django.db import models

from users_app.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='E-mail')
    name = models.CharField(max_length=250, verbose_name='ФИО')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


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
        (STATUS_STARTED, 'запущена'),
        (STATUS_COMPLETED, 'завершена'),
    )

    mailing_time = models.TimeField(verbose_name='Время отправки')
    period = models.CharField(max_length=50, choices=PERIODS, verbose_name='Периодичность')
    status = models.CharField(max_length=50, choices=STATUSES, verbose_name='Статус')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')

    def __str__(self):
        return f'{self.pk}. Время: {self.mailing_time}, период: {self.period}, статус: {self.status}, клиенты: {self.clients.all()}.'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, **NULLABLE, verbose_name='Рассылка')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class MailingLog(models.Model):
    time = models.DateField(auto_now=True, verbose_name='Время изменения')
    status = models.BooleanField(default=False, verbose_name='Статус попытки')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    error_msg = models.TextField(**NULLABLE, verbose_name='Сообщение об ошибке')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL')
    text = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='media/', **NULLABLE, verbose_name="Превью")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name="Пользователь")

    def __str__(self):
        return f'{self.name}, {self.slug}'

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
