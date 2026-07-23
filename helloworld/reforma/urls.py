from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_reforma, name='listar_reforma'),
    path('criar/', views.criar_reforma, name='criar_reforma'),
]
