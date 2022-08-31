from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('cadastro/', views.CadastroPlantas.as_view(), name='cadastroPlantas'),
    path('lista/', views.ListaPlantas.as_view(), name='listaPlantas'),
    path('editar/<int:pk>', views.editarPlantas, name='editarPlantas'),
    path('deletar/<int:pk>',views.deletarPlanta, name='deletar'),
]
