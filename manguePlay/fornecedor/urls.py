from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('listar/', views.listar_fornecedores, name='listar_fornecedores'),
]
