from django import forms
from my_app.models import Person

class Appform(forms.Form):
    name = forms.CharField(label="name of user", max_length=10)
    age = forms.CharField(label="enter your name here", max_length=50)
    address = forms.CharField(label="address", max_length=100)
    hobies = (('Managa', 'Managa'),
              ('Anime', 'Anime'),
              ('Sieries', 'Sieries'))
    field = forms.ChoiceField(choices=hobies)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

class LoginForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["user_name", "password"]