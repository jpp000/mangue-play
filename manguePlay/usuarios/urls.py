from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('usuario/', views.usuario_pag, name='user_dashboard'),
    path('admin_login/', views.admin_pag, name='admin_dashboard'),
]