from django.shortcuts import render
from secao.models import Secao
from subsecao.models import Subsecao
from noticias.models import Noticia

def index(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by("ordem")
    noticias = Noticia.objects.all().order_by("-id")[0:3]

    noticia_format = []

     


    for noticia in noticias:

        # titulo = noticia.titulo = 
        ...

    return render(request,'inicio/index.html',{

        "secoes":secoes,
        "subsecoes":subsecoes,
        "noticias":noticias
    })