from re import sub
from django.shortcuts import render
from subsecao.models import Subsecao

def cadastroSubsecao(request,id_secao):

    subsecoes = Subsecao.objects.all()
    cont_subsecoes = list(range(1,len(subsecoes)+2))
    max_ordem = len(subsecoes)+1

    return render(request,'subsecao/index.html',{"subsecoes":subsecoes,"cont_subsecoes":cont_subsecoes,"max_ordem":max_ordem})
