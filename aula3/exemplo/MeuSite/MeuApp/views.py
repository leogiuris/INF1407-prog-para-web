from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
    return render(req,"MeuApp/home.html")

def about(req):
    return render(req,"MeuApp/about.html")