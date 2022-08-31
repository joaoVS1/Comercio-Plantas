from pyexpat import model
from django.db import models

# Create your models here.
class Planta(models.Model):
    nome = models.CharField(max_length=50)
    nome_cientifico = models.CharField(max_length=50)
    origem = models.CharField(max_length=50)
    preco = models.FloatField(default=1.99)
    imageurl = models.TextField(max_length=500, default='')
    descricao = models.TextField(max_length=500, default='')

    def __str__(self) -> str:
        return self.nome