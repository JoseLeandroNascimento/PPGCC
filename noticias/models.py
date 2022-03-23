from pyexpat import model
from unittest.mock import DEFAULT
from django.db import models
from usuario.models import Usuario
from upload.models import Arquivo

class Noticia(models.Model):
    
    titulo = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )
    previa = models.TextField(
        null=False,
        blank = False
    )

    img = models.ForeignKey(

        Arquivo,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        unique=False

    )

    conteudo = models.TextField(
        null = False,
        blank = False
    )
    
    # relacionamento com upload

    usuario = models.ForeignKey(
        
        Usuario,
        unique=False,
        on_delete=models.SET_NULL,
        null=True,
        blank = False
    )

    data_publicacao = models.DateTimeField(
        auto_now = True
    )

