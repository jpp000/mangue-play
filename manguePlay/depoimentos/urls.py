from django.urls import path
from .views import depoimentos_view

urlpatterns = [
    path('depoimentos/', depoimentos_view, name='depoimentos'),
]
