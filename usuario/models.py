from pyexpat import model
from unittest.mock import DEFAULT
from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(
        max_length = 100, 
        null = False,
        blank = False
    )
    senha = models.CharField(
        max_length = 10,
        null = False,
        blank = False
    )
    permissao = models.IntegerField(
        null = False,
        blank = False
        
    )
    ativado = models.BooleanField(
        null = False,
        blank = False,
        default = True
    )
    data_cadastro = models.DateField(
        auto_now = True
    )