from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import Appform

def froma(request):
    form = Appform()
    return render(request, 'form.html', {'f':form})