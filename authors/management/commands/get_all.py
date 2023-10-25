from django.core.management.base import BaseCommand

from lec2app.models import User


class Command(BaseCommand):
    help = "Return all users"

    def handle(self, *args, **kwargs):
        result = User.objects.all()
        self.stdout.write(f"{result}")
