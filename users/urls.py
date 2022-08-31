from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.CadastroUsers.as_view(), name='cadastroUsers'),
    path('login', views.Login.as_view(), name='login'),
    path('sair/', views.sair, name='sair'),
]
