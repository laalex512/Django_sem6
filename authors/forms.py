import datetime
from django import forms


class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    biography = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    birthday = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
