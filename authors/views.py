from django.shortcuts import render
from authors.models import Author, Post
from .forms import AuthorForm


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid:
            author = Author(
                first_name=form.cleaned_data("first_name"),
                last_name=form.cleaned_data("last_name"),
                email=form.cleaned_data("email"),
                biography=form.cleaned_data("biography"),
                birthday=form.cleaned_data("birthday"),
            )
            author.save()
            return get_posts_by_author(request, author.id)
    else:
        form = AuthorForm()
    return render(request, "authors/add_author.html", {"form": form})


def get_posts_by_author(request, author_id):
    author = Author.objects.filter(pk=author_id).first()
    posts = Post.objects.filter(author_id=author)
    context = {"posts": [], "author": str(author)}
    for post in posts:
        context["posts"].append(post)
    return render(request, "authors/get_posts.html", context)


def get_post(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    post.count_views += 1
    post.save()
    context = {"post": post}
    return render(request, "authors/get_post.html", context)
