from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_brinquedo/', views.adicionar_brinquedo, name='adicionar_brinquedo'),
    path('visualizar_brinquedos/', views.visualizar_brinquedos, name='visualizar_brinquedos'),
    path('visualizar_brinquedos_admin/', views.visualizar_brinquedos_admin, name='visualizar_brinquedos_admin'),
    path('editar_brinquedo/', views.editar_brinquedo, name='editar_brinquedo'),
    path('selecionar_brinquedo/<int:id>/', views.selecionar_brinquedo, name='selecionar_brinquedo'),
    path('excluir_brinquedo/<int:id>/', views.excluir_brinquedo, name='excluir_brinquedo'),
]
