from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "t1app/index.html")


def about(request):
    context = {"name": "Alex"}
    return render(request, "t1app/about.html", context)
