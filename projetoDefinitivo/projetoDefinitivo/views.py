from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View


def home(request):
    return render(request, 'projetoDefinitivo/index.html')

def homeSec(request):
    return render(request,"seguranca/secHome.html")