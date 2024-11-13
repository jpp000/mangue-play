from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_encomenda, name='adicionar_encomenda'),
    path('visualizar/', views.visualizar_encomendas, name='visualizar_encomendas'),
    path('excluir/<int:encomenda_id>/', views.excluir_encomenda, name='excluir_encomenda'),
    path('editar_encomenda/<int:id>/', views.editar_encomenda, name='editar_encomenda'),
]