import datetime

from django.conf import settings
from django.core.mail import send_mail

from mailing_app.models import Message, Mailing, MailingLog


def prepare_mailing(mailing_object):
    if mailing_object.status == 'created':
        if mailing_object.mailing_time <= datetime.datetime.now().time():
            mailing_object.status = 'started'
            mailing_object.save()
    if mailing_object.status == 'started':
        clients = mailing_object.clients.all()
        clients_list = [client.email for client in clients if client.email]
        try:
            send_mail(
                subject=Message.objects.filter(mailing=mailing_object).first().subject,
                message=Message.objects.filter(mailing=mailing_object).first().body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=clients_list,
                fail_silently=False,
            )
            log = MailingLog.objects.create(status=True, mailing=mailing_object)
            log.save()
        except Exception as e:
            result = e
            log = MailingLog.objects.create(mailing=mailing_object, error_msg=result)
            log.save()


def send_mailing():
    mailing_list = Mailing.objects.all()

    for mailing_object in mailing_list:
        if mailing_object.status != 'completed':
            log = MailingLog.objects.all().filter(mailing=mailing_object).last()

            if log is None:
                prepare_mailing(mailing_object)

            elif log.time != datetime.datetime.now().date() or not log.status:

                if mailing_object.period == 'daily':
                    prepare_mailing(mailing_object)
                elif mailing_object.period == 'weekly':
                    if log.time.weekday() == datetime.datetime.now().weekday():
                        prepare_mailing(mailing_object)
                elif mailing_object.period == 'monthly':
                    if log.time.day == datetime.datetime.now().day:
                        prepare_mailing(mailing_object)
