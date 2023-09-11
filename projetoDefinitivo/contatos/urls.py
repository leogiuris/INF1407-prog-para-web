from django.urls.conf import path
from contatos import views


app_name = "contatos"

urlpatterns = [
    path('cria/', views.ContatoCreateView.as_view(),name='cria-contato'),
    path('atualiza/<int:pk>', views.ContatoUpdateView.as_view(),name='atualiza-contato'),
    path('remove/<int:pk>', views.ContatoDeleteView.as_view(),name='remove-contato'),
    path('lista/', views.ContatoListView.as_view(),name='lista-contatos'),
    path('', views.ContatoListView.as_view(),name='home-contatos'),
]