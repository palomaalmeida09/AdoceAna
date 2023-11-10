from django.urls import path, include
from django.contrib.auth.models import User
from . import views 
app_name = "usuarios"
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.entrar, name="login"),
]