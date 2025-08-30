from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse
from .forms import Appform, PersonForm, LoginForm
from .models import Person

def users(request):
    try:
        persons = Person.objects.all()
    except:
        return HttpResponse(content="<h1>you don't have any users<h1>")
    return  render(request, 'users.html', {'users': persons})

def home(request):
    return render(request, 'home.html', {})

def welcome(request, name):
    return render(request, "welcome.html", {'name' : name})

def register(request):
    f = PersonForm()
    if request.method == "POST":
        f = PersonForm(request.POST)
        if f.is_valid():
            try:
                person = Person.objects.get(user_name = f.data.get("user_name"))
            except:
                f.save()
                return HttpResponse(content="<h1>account created !</h1><br/><a href='/login'>login</a>")
            return HttpResponse(content="<h1>username taken</h1>")
    return render(request, 'register.html', {'f':f})

def login(request):
    form = LoginForm()

    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            try:
                person = Person.objects.get(user_name = f.data.get("user_name"))
                if  person.user_name == f.data.get("user_name") and person.password == f.data.get("password"):
                    return  welcome(request, person.user_name)
            except:
                return HttpResponse(content="<h1>wrong credientials</h1>")
            render(request, "welcome.html", {'name': person.user_name})

    return render(request, "login.html", {'form' : form})