from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Команда для создания админа в проекте"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@example.com',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('123qwe')
        user.save()
