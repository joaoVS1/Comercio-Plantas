from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.comprar, name='comprar'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'), 
    path('add_carrinho', views.add_carrinho, name='add_carrinho'),
    path('planta/<int:pk>', views.PaginaProduto.as_view(), name='paginaProduto'),
    path('pagamento/', views.pagamento, name='pagamento'),
    path('removerCarrinho/<int:pk>', views.removerCarrinho, name='remover')
]
