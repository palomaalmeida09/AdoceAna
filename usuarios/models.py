from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario (models.Model):
    nome = models.CharField("Nome", max_length=50)
    email = models.EmailField("Email")
    telefone = models.CharField("Telefone", max_length=11)
    login = models.OneToOneField(User, on_delete=models.CASCADE)