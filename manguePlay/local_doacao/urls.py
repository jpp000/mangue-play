from django.urls import path
from . import views

urlpatterns = [
    path('local', views.local_doacao, name='local_doacao'),  
    path('adicionar_doacao/', views.adicionar_doacao, name='adicionar_doacao'),
    path('usuario/', views.adicionar_doacao, name='user_dashboard'),   # Nova URL para salvar a doação
]
