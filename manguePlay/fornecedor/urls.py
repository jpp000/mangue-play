# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('listar/', views.listar_fornecedores, name='listar_fornecedores'),
    path('editar/<int:pk>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('excluir/<int:pk>/', views.excluir_fornecedor, name='excluir_fornecedor'),
    path('login/', views.login_view, name='login'),  # Defina uma URL de login
]