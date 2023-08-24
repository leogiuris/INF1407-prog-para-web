from django.shortcuts import render
from django.views.generic.base import View

def home(req):
    return render(req,'Homepage/home.html')