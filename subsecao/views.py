from re import sub
from django.shortcuts import redirect, render
from secao.models import Secao
from subsecao.models import Subsecao
from usuario.models import Usuario

def cadastroSubsecao(request,id_secao):

    subsecoes = Subsecao.objects.all()
    cont_subsecoes = list(range(1,len(subsecoes)+2))
    max_ordem = len(subsecoes)+1
    usuario_logado = request.session.get('id_usuario')
    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    return render(request,'subsecao/index.html',{"id_secao":id_secao,"subsecoes":subsecoes,"cont_subsecoes":cont_subsecoes,"max_ordem":max_ordem,"usuario_logado":usuario_logado,"secoes":secoes,"subsecoes":subsecoes})

def salvarSubsecao(request):

    if(request.method == 'POST'):

        titulo = request.POST.get('titulo')
        ordem = request.POST.get('ordem')
        ativa = request.POST.get('ativada')
        id_usuario = request.POST.get('id_usuario')
        id_secao = request.POST.get('id_secao')

        usuario = Usuario.objects.get(id=id_usuario)
        secao = Secao.objects.get(id=id_secao)


        subsecoes = Subsecao.objects.filter(secao=secao).order_by('ordem')

        for sub in subsecoes:

            if sub.ordem >= int(ordem):

                sub.ordem = sub.ordem + 1
                sub.save()
            
        
        novaSubsecao = Subsecao(titulo=titulo,ordem=ordem,ativo=ativa,secao=secao,usuarios=usuario)

        novaSubsecao.save()



        
    
    return redirect('/home')

    
def subsecao(request,id_subsecao):

    sub = Subsecao.objects.get(id=id_subsecao)
    subsecoes = Subsecao.objects.all().order_by('ordem')
    conteudo = sub.conteudo

    return render(request,'subsecao/view.html',{

        "conteudo":conteudo,
        "subsecao":subsecao,
        'subsecoes':subsecoes
    })

