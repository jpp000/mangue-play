from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_encomenda, name='adicionar_encomenda'),
]
