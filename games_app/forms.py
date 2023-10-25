from django import forms

GAMES = [("E", "eagle"), ("C", "cube"), ("R", "rand_num")]


class GameChoiceForm(forms.Form):
    select_game = forms.ChoiceField(choices=GAMES)
    select_count = forms.IntegerField(min_value=1, max_value=64)
