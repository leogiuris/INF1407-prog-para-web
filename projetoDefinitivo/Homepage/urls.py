from django.urls.conf import path
from Homepage import views

urlpatterns = [
    path('',views.home)
]