from django.urls import path
from . import views

urlpatterns = [
    path('local', views.local_doacao, name='local_doacao'),  
    path('adicionar_doacao/', views.adicionar_doacao, name='adicionar_doacao'),
    path('visualizar_local/', views.visualizar_local, name='visualizar_local'),
    path('local_doacao/editar_doacao/<int:pk>/', views.editar_doacao, name='editar_doacao'), 
    path('local_doacao/deletar_doacao/<int:pk>/', views.deletar_doacao, name='deletar_doacao'),
    path('infolocal/', views.infolocal, name='infolocal'),
]