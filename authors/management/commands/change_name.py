from django.core.management.base import BaseCommand
from lec2app.models import User


class Command(BaseCommand):
    help = "Return user by id"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")
        parser.add_argument("name", type=str, help="New Name")

    def handle(self, *args, **kwargs):
        pk = kwargs.get("pk")
        name = kwargs.get("name")
        user = User.objects.filter(pk=pk).first()
        if user:
            user.name = name
            user.save()
            self.stdout.write(f"{user}")
        else:
            self.stdout.write(f"User with id = {pk} doesn't exists")
