from django.core.management.base import BaseCommand
from lec2app.models import User


class Command(BaseCommand):
    help = "Return user by id"

    def add_arguments(self, parser):
        parser.add_argument("start", type=int, help="start ID")
        parser.add_argument("end", type=int, help="end ID")

    def handle(self, *args, **kwargs):
        start_id = kwargs.get("start")
        end_id = kwargs.get("end")
        result = User.objects.filter(pk__range=[start_id, end_id])
        if result:
            for user in result:
                self.stdout.write(f"{user}")
        else:
            self.stdout.write(f"User with id = {start_id} doesn't exists")
