from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('crearContratos/', views.SCcreator, name="contracts"),
    path('verContratos/', views.verContratos, name="dummy")
]