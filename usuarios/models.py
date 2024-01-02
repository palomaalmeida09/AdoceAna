from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario (models.Model):
    nome = models.CharField("Nome", max_length=50)
    telefone = models.CharField("Telefone", max_length=11)
    acesso = models.OneToOneField(User, on_delete=models.CASCADE)


from django.db import models

class Produto(models.Model):
    img = models.ImageField(upload_to='produtos/')
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    qtd = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo