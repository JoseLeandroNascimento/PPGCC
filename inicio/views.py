from django.shortcuts import redirect, render
from secao.models import Secao
from subsecao.models import Subsecao
from noticias.models import Noticia
from defesa.models import Defesa


# Essa view controla a pagina principal do site
def index(request):

    secoes = Secao.objects.filter(ativada=True).order_by('ordem')
    subsecoes = Subsecao.objects.filter(ativo=True).order_by("ordem")

    # As duas linhas de código abaixo buscam os registros mais recentes para serem mostrados
    # Na pagina home
    defesas = Defesa.objects.all().order_by('-id')[0:3]
    noticias = Noticia.objects.all().order_by("-id")[0:3]

    return render(request,'inicio/index.html',{

        "secoes":secoes,
        "subsecoes":subsecoes,
        "noticias":noticias,
        "defesas":defesas
    })



def viewNoticia(request,noticia):

    secoes = Secao.objects.filter(ativada=True).order_by('ordem')
    subsecoes = Subsecao.objects.filter(ativo=True).order_by("ordem")

    # Caso o id passado for invalido é tratado erro aqui
    try:
    
        noticia = Noticia.objects.get(id = noticia)

    except:

        # O usuario é redirecionado para pagina home do site
        return redirect('/')
    
    return render(request, 'inicio/view-noticia.html',{

        "secoes":secoes,
        "subsecoes":subsecoes,
        "noticia":noticia
       
    })


# Mostra todas as noticias
def viewNoticias(request):

    secoes = Secao.objects.filter(ativada=True).order_by('ordem')
    subsecoes = Subsecao.objects.filter(ativo=True).order_by("ordem")
    noticias = Noticia.objects.all().order_by('-id')

    return render(request, 'inicio/view-noticias.html',{

        "secoes":secoes,
        "subsecoes":subsecoes,
        "noticias":noticias
       
    })

# Essa view mostra todas as defesas
def viewDefesas(request):

    secoes = Secao.objects.filter(ativada=True).order_by('ordem')
    subsecoes = Subsecao.objects.filter(ativo=True).order_by("ordem")
    defesas = Defesa.objects.all().order_by('-id')

    return render(request,"inicio/view-defesas.html",{

        "secoes":secoes,
        "subsecoes":subsecoes,
        "defesas":defesas
        
    })


def viewDefesa(request,defesa_id):

    secoes = Secao.objects.filter(ativada=True).order_by('ordem')
    subsecoes = Subsecao.objects.filter(ativo=True).order_by("ordem")

    try:

        defesa = Defesa.objects.get(id=defesa_id)

    except:

        return redirect('/view-defesas/')

    
    return render(request,'inicio/view_defesa.html',{

        'secoes':secoes,
        'subsecoes':subsecoes,
        'defesa':defesa
    })


def viewSecao(request,subsecao_id):

    secoes = Secao.objects.filter(ativada=True).order_by('ordem')
    subsecoes = Subsecao.objects.filter(ativo=True).order_by("ordem")

    try:

        subsecao = Subsecao.objects.get(id=subsecao_id)

    except:

        return redirect('/')

    
    return render(request,'inicio/view_subsecao.html',{

        'secoes':secoes,
        'subsecoes':subsecoes,
        'subsecao':subsecao
    })
