from django.urls import path
from . import views
urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("cadastro/", views.cadastro, name='cadastro'),
    path("lista/", views.lista, name='lista'),
]
