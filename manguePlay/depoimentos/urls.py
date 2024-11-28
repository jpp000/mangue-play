from django.urls import path
from .views import (
    depoimentos_view,
    adicionar_depoimento_view,
    depoimentos_admin_view,  # Importando a nova view para administração
)

urlpatterns = [
    path('depoimentos/', depoimentos_view, name='depoimentos'),  # Exibe os depoimentos
    path('adicionar-depoimento/', adicionar_depoimento_view, name='adicionar_depoimento'),
    path('admin-depoimento/', depoimentos_admin_view, name='depoimentos_admin'),  # Nova rota para admin
]
