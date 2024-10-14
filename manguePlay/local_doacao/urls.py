from django.urls import path
from . import views

urlpatterns = [
    path('local', views.local_doacao, name='local_doacao'),  
]
