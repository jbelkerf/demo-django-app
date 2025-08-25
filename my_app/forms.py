from django import forms

class Appform(forms.Form):
    name = forms.CharField(label="name of user", max_length=10)
    age = forms.CharField(label="enter your name here", max_length=50)
    address = forms.CharField(label="address", max_length=100)
    hobies = (('Managa', 'Managa'),
              ('Anime', 'Anime'),
              ('Sieries', 'Sieries'))
    field = forms.ChoiceField(choices=hobies)

