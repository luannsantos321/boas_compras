from django.urls import path
from .views import inicio, cadastro, lista, update_lista, delete_id_lista, delete_lista

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cadastro/', cadastro, name='cadastro'),
    path('lista/', lista, name='lista'),
    path('update_lista/<int:id>/', update_lista, name='update_lista'),
    path('delete_id_lista/<int:id>/', delete_id_lista, name='delete_id_lista'),
    path('delete_lista/', delete_lista, name='delete_lista'),

]