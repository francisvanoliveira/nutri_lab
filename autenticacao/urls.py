from os import name
from django.urls import URLPattern, path
from . import views

urlpatterns = [
  path('cadastro/', views.cadastro, name="cadastro"),
  path('logar/', views.logar, name="logar")
]