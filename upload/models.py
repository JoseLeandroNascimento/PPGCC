from django.db import models



class Arquivo(models.Model):

    url = models.FileField(upload_to='uploads/',null=False,blank=False)
    nome = models.TextField(max_length=100,null=False)
    extensao = models.TextField(max_length=10,blank=False)
    tipo_arquivo = models.CharField(max_length=100, null=False)
    data = models.DateTimeField(auto_now=True)
