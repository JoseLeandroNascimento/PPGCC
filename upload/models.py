from django.db import models
from numpy import blackman

from usuario.models import Usuario



class Arquivo(models.Model):

    url = models.FileField(upload_to='uploads/',null=False,blank=False)
    nome = models.TextField(max_length=100,null=False)
    extensao = models.TextField(max_length=10,blank=False)
    data = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(

        Usuario,
        null= True,
        on_delete= models.SET_NULL,

    )
