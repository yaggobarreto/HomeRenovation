from django.urls import path

from . import views

urlpatterns = [
    path('', views.usuarios_app, name='usuarios_app'),
]
