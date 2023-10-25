from django.urls import path
from . import views

urlpatterns = [
    path("eagle/<int:count>", views.eagle, name="eagle"),
    path("cube/<int:count>", views.cube, name="cube"),
    path("rand_num/<int:count>", views.rand_num, name="rand_num"),
    path("", views.index, name="index"),
]
