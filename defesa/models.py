from django.db import models


class Defesa(models.Model):

    titulo = models.CharField(

        max_length= 100,
        unique= True,
        null=False,
        blank=False

    )

    local = models.CharField(

        max_length= 100,
        null=False,
        blank=False

    )

    horario = models.DateTimeField(

        null=False,
        blank=False

    )

    conteudo = models.TextField(


    )

    data_criacao =  models.DateTimeField(
        auto_now=True
    )


    
