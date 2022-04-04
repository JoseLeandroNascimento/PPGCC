from django.db import models
from usuario.models import Usuario


class Secao(models.Model):

    titulo = models.CharField(
        
        unique=True,
        max_length= 200,
        null = False,
        blank = False
        
    )

    icon = models.CharField(

        max_length= 100,
        null = False,
        blank = False

    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL, 
        null = True
    )


    ordem = models.IntegerField()

    ativada = models.BooleanField(

        default=True,
        
    )

    data_criacao = models.DateTimeField(auto_now=True)
    
    usuarios = models.ManyToManyField(Usuario,related_name="+")