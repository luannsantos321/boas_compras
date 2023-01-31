from django.urls import path
from .views import inicio, lista, cadastro, update_produto,delete_produto
urlpatterns = [
    path('', inicio, name='inicio'),
    path('lista/', lista, name='lista'),
    path('cadastro/', cadastro, name='cadastro'),
    path('update_produto/<int:id>/', update_produto, name='update_produto'),
    path('delete_produto/<int:id>/', delete_produto, name='delete_produto'),
]