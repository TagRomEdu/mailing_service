from django.conf import settings
from django.core.mail import send_mail

from mailing_app.models import Message


def send_mailing(mailing_object):
    clients = mailing_object.clients.all()
    clients_list = [client.email for client in clients if client.email]
    send_mail(
        subject=Message.objects.filter(mailing=mailing_object).first().subject,
        message=Message.objects.filter(mailing=mailing_object).first().body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=clients_list,
        fail_silently=False,
    )
    settings.CRONJOBS.append(1)