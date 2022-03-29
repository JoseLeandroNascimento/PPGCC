
from django.db import models
from secao.models import Secao
from usuario.models import Usuario


class Subsecao(models.Model):

    secao = models.ForeignKey(

        Secao,
        blank=False,
        null=False,
        on_delete= models.CASCADE,
       
    )

    titulo = models.CharField(

        max_length= 300,
        null = False,
        unique=True,
        blank=False
    )

    conteudo = models.TextField()

    ordem = models.IntegerField(unique=True)

    usuarios = models.ForeignKey(

        Usuario,
        on_delete=models.SET_NULL,
        blank=False,
        null=True
    )

    ativo = models.BooleanField(default=True)


