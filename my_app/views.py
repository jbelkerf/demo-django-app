from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import Appform, PersonForm

def froma(request):
    form = Appform()
    f = PersonForm()
    return render(request, 'form.html', {'f':f})