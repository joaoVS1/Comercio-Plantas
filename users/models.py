from argparse import _MutuallyExclusiveGroup
import email
from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    adm = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome