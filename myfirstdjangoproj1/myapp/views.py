from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    s = "<h1>Hi.. Welcome to Django World!</h1>"
    return HttpResponse(s)

def display2(request):
    s = "<h1>Hi.. Welcome to Django World! from display2()</h1>"
    return HttpResponse(s)