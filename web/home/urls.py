from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contract/', views.SCcreator, name="contracts"),
    path('dummy/', views.postearDummy, name="dummy")
]