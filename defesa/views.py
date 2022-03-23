from os import sep
from django.shortcuts import redirect, render
from django.db.models import Q
from  defesa.models import  Defesa
from secao.models import Secao
from usuario.models import Usuario

def defesa(request):

    defesas = Defesa.objects.all()
    secoes = Secao.objects.all().order_by('ordem')

    # usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))


    # return render(request, 'defesa/index.html',{'defesas':defesas,"secoes":secoes,'usuario_logado':usuario_logado})
    return render(request, 'defesa/index.html',{'defesas':defesas,"secoes":secoes})


def cadatroDefesa(request):

    secoes = Secao.objects.all().order_by('ordem')
    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    return render(request,"defesa/cadastroDefesa.html",{"secoes":secoes,'usuario_logado':usuario_logado})

def salvarDefesa(request):

    if(request.method == 'POST'):

        dados = request.POST

        titulo = dados.get('titulo')
        local  = dados.get('local')
        horario = dados.get('horario')
        conteudo = dados.get('conteudo')

        novaDefesa = Defesa(titulo=titulo,local=local,horario=horario,conteudo=conteudo)

        novaDefesa.save()

        

    return redirect('/defesa/')



def excluirDefesa(request):


    if(request.method == 'POST'):

        id = request.POST.get('id_defesa')

        defesa = Defesa.objects.filter(id=id).first()

        defesa.delete()
    
    return redirect("/defesa/")


def buscarDefesas(request):

    secoes = Secao.objects.all().order_by('ordem')

    if request.method =='POST':

        valor_pesquisa = request.POST.get('valor_pesquisa')

        defesas = Defesa.objects.filter(Q(titulo__icontains=valor_pesquisa) | Q(local__icontains=valor_pesquisa))

    
    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    return render(request,'defesa/index.html',{'defesas':defesas,"secoes":secoes,'usuario_logado':usuario_logado})


def editarDefesa(request):

    secoes = Secao.objects.all().order_by('ordem')
    
    if(request.method == 'POST'):

        defesa_id = request.POST.get('defesa_id')

        defesa = Defesa.objects.get(id = defesa_id)


    
    
    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))


    return render(request,"defesa/editarDefesa.html",{'defesa':defesa,"secoes":secoes,'usuario_logado':usuario_logado})


def updateDefesa(request):

    if(request.method == 'POST'):

        dados = request.POST

        titulo = dados.get('titulo')
        local  = dados.get('local')
        horario = dados.get('horario')
        conteudo = dados.get('conteudo')
        id_usuario = dados.get('id_usuario')
        id_defesa = dados.get('id_defesa')


        defesa = Defesa.objects.filter(id=id_defesa).first()

        if(defesa):

            defesa.titulo = titulo
            defesa.local = local
            defesa.horario = horario
            defesa.conteudo = conteudo

            defesa.save()


    return redirect('/defesa/')