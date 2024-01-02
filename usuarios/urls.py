from django.urls import path, include
from django.contrib.auth.models import User
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.entrar, name="login"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('cad_produto/', views.cad_produto, name="cad_produto"),
    path('comprar/<int:id>', views.comprar, name="comprar"),
]