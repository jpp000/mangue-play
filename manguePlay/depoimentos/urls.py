from django.urls import path
from .views import depoimentos_view, adicionar_depoimento_view

urlpatterns = [
    path('depoimentos/', depoimentos_view, name='depoimentos'),  # Exibe os depoimentos
    path('adicionar-depoimento/', adicionar_depoimento_view, name='adicionar_depoimento'),  # Adiciona um novo depoimento
]
