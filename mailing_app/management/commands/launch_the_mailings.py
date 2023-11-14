from django.core.management import BaseCommand

from mailing_app.cron import send_mailing


class Command(BaseCommand):
    def handle(self, *args, **options):
        return send_mailing()
