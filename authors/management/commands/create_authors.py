import datetime
import random
from django.core.management.base import BaseCommand, CommandParser

from authors.models import Author, Post


class Command(BaseCommand):
    help = "Created authors and posts"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("count", type=int, help="Count authors")
        return super().add_arguments(parser)

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        for i in range(1, count + 1):
            author = Author(
                first_name=f"FName{i}",
                last_name=f"LName{i}",
                email=f"email{i}@gmail.com",
                biography="Bla bla bla",
                birthday=datetime.datetime.now(),
            )
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f"Title{j}",
                    content=f"Text from {author} #{j} is bla bla bla many long text",
                    author=author,
                    category=f"Category {j}",
                    count_views=random.randint(0, 100),
                    is_published=random.choice([True, False]),
                )
                post.save()

        self.stdout.write(f"{count} authors and posts created")
