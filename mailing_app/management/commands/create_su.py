from django.core.management import BaseCommand
from users_app.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.com',
            first_name='Admin',
            last_name='Adminin',
            is_superuser=True,
            is_staff=True
        )

        user.set_password('0123456789')
        user.save()
