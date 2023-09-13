"""
URL configuration for projetoDefinitivo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from projetoDefinitivo import views
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy


urlpatterns = [
    path('', views.home,name='home-page'),

    path('contatos/',include ('contatos.urls'),name="homepage"),

    path('admin/', admin.site.urls),

    path('seguranca/', views.homeSec,name='sec-home'),

    path('seguranca/login', LoginView.as_view(
            template_name='seguranca/usuario.html',
            extra_context={
                'titulo':'Login',
                'tituloPagina':'Login',
                'textoBotao':'Login',
            }
        ),name='sec-login'),

    path('seguranca/logout', LogoutView.as_view(next_page=reverse_lazy('sec-home')
        ),name='sec-logout'),

    path('seguranca/registro', views.registro ,name='sec-registro'),

    path('seguranca/troca_senha', PasswordChangeView.as_view(
        template_name = 'seguranca/usuario.html',
        extra_context = {
            'titulo':'Troca de Senha',
            'tituloPagina':'Troca de senha',
            'textoBotao':'Troca senha',
        },
        success_url=reverse_lazy('sec-password_change_done'),
    ) ,name='sec-password_change'),

    path('seguranca/troca_senha_finalizada/',
        PasswordChangeView.as_view(
            template_name="seguranca/password_change_done.html"), 
        name='sec-password_change_done'),

    path('seguranca/terminaRegistro/<int:pk>',
        UpdateView.as_view(
            template_name= 'seguranca/usuario.html',
            success_url=reverse_lazy('sec-home'),
            extra_context = {
            'titulo':'Termina Registro',
            'tituloPagina':'Termina Registro',
            'textoBotao':'Atualiza',},
            model=User,
            fields=[
                'first name','last name','email'
            ],
        ), name='sec-completaDadosUsuario',
    ),

]


