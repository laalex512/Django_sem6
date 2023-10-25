from django.urls import path
from . import views

urlpatterns = [
    path("posts/<int:author_id>/", views.get_posts_by_author, name="posts"),
    path("post/<int:post_id>/", views.get_post, name="post"),
    path("add_author", views.add_author, name="add_author"),
]
