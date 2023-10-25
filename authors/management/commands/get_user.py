from django.core.management.base import BaseCommand
from lec2app.models import User


class Command(BaseCommand):
    help = "Return user by id"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")

    def handle(self, *args, **kwargs):
        pk = kwargs["pk"]
        result = User.objects.filter(pk=pk).first()
        if result:
            self.stdout.write(f"{result}")
        else:
            self.stdout.write(f"User with id = {pk} doesn't exists")
