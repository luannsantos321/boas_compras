from django.urls import path
from .views import inicio, lista, cadastro, \
    update_produto, delete_produto, delete_produto_all, cadastro_valor,delete_valor, soma
urlpatterns = [
    path('', inicio, name='inicio'),
    path('lista/', lista,  name='lista'),
    path('cadastro/', cadastro, name='cadastro'),
    path('update_produto/<int:id>/', update_produto, name='update_produto'),
    path('delete_produto/<int:id>/', delete_produto, name='delete_produto'),
    path('delete_produto_all/', delete_produto_all, name='delete_produto_all'),
    path('cadastro_valor/', cadastro_valor, name='cadastro_valor'),
    path('delete_valor/<int:id>/', delete_valor, name='delete_valor'),
    path('soma/', soma,  name='soma'),
]