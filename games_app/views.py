from django.shortcuts import render
import logging
import random
from .forms import GameChoiceForm


logger = logging.getLogger(__name__)


def index(request):
    if request.method == "POST":
        form = GameChoiceForm(request.POST)
        if form.is_valid():
            select_game = form.cleaned_data["select_game"]
            select_count = form.cleaned_data["select_count"]
            match select_game:
                case "E":
                    return eagle(request, select_count)
                case "C":
                    return cube(request, select_count)
                case "R":
                    return rand_num(request, select_count)
    else:
        form = GameChoiceForm()
    return render(request, template_name="games_app/index.html", context={"form": form})


def eagle(request, count):
    result_list = []
    for _ in range(count):
        result_list.append(random.choice(["heads", "tails"]))
    context = {
        "throws_list": result_list,
        "game_results": f"List of {count} throws coin toss:",
        "game_type": "Coin toss",
    }
    return render(request, "games_app/games.html", context)


def cube(request, count):
    result_list = []
    for _ in range(count):
        result_list.append(random.randint(1, 6))
    context = {
        "throws_list": result_list,
        "game_results": f"List of {count} throws cube toss: ",
        "game_type": "Cube toss",
    }
    return render(request, "games_app/games.html", context)


def rand_num(request, count):
    result_list = []
    for _ in range(count):
        result_list.append(random.randint(0, 100))
    context = {
        "throws_list": result_list,
        "game_results": f"List of {count} random numbers: ",
        "game_type": "Random Number",
    }
    return render(request, "games_app/games.html", context)
