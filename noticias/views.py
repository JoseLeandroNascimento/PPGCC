
from django.shortcuts import redirect, render
from noticias.models import Noticia
from secao.models import Secao
from usuario.models import Usuario
from upload.models import Arquivo
from django.contrib import messages




def noticias(request):

    secoes = Secao.objects.all().order_by('ordem')
    noticias = Noticia.objects.all()

    try:

        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

    except:

        usuario_logado = None

    return render(request, "noticias/index.html", {"noticias": noticias, "secoes": secoes, 'usuario_logado': usuario_logado})


def add_noticia(request):

    secoes = Secao.objects.all().order_by('ordem')
    imagens = Arquivo.objects.filter(tipo_arquivo = 'imagem')

    try:

        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

    except:

        usuario_logado = None

    return render(request, "noticias/add_noticia.html", {"secoes": secoes, 'usuario_logado': usuario_logado, 'imagens': imagens})


def salvar_noticia(request):

    if(request.method == "POST"):

        titulo = request.POST.get("titulo")
        previa = request.POST.get("previa")
        conteudo = request.POST.get("conteudo")
        img_id = request.POST.get('img_id')

        print(img_id)
        if(img_id == '-1'):

            messages.add_message(request, messages.WARNING,"É necessário fornecer uma imagem")
            return redirect("/noticias/")

        else:

            img = Arquivo.objects.get(id = img_id )

            print(img_id)
            print(img.nome)
            try:
                                
                usuario = Usuario.objects.get(
                id=request.session.get('id_usuario'))

            except:

                usuario = None

            novaNoticia = Noticia(titulo= titulo, previa = previa, conteudo=conteudo, img= img, usuario = usuario)
            novaNoticia.save()

    return redirect("/noticias/")


def excluir_noticia(request):

    if(request.method == "POST"):
        id = request.POST.get("id_noticia")
        noticia = Noticia.objects.filter(id=id).first()
        noticia.delete()
    return redirect("/noticias/")


def editar_noticia(request):

    secoes = Secao.objects.all().order_by('ordem')
    imagens = Arquivo.objects.filter(tipo_arquivo = 'imagem')


    if(request.method == "POST"):

        id = request.POST.get("id_noticia")
        noticia = Noticia.objects.filter(id=id).first()


    try:

        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

    except:

        usuario_logado = None

    return render(request, "noticias/editar_noticia.html", {"noticia": noticia, "secoes":secoes,'usuario_logado':usuario_logado,'imagens':imagens})


def update_noticia(request):

    if(request.method == "POST"):
        id_noticia = request.POST.get("id_noticia")
        titulo = request.POST.get("titulo")
        previa = request.POST.get("previa")
        conteudo = request.POST.get("conteudo")
        id_usuario = request.POST.get("id_usuario")
        img_id = request.POST.get('img_id')

        img = Arquivo.objects.get(id = img_id)
        noticia = Noticia.objects.filter(id=id_noticia).first()
        noticia.titulo = titulo
        noticia.previa = previa
        noticia.conteudo = conteudo
        noticia.id_usuario = id_usuario
        noticia.img = img
        noticia.save()

    return redirect("/noticias/")


def buscarNoticia(request):

    secoes = Secao.objects.all().order_by('ordem')

    if(request.method == 'POST'):

        valor_pesquisa = request.POST.get('valor_pesquisa')

        noticias = Noticia.objects.all().filter(titulo__icontains=valor_pesquisa)

    try:

        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

    except:

        usuario_logado = None

    return render(request, "noticias/index.html", {'noticias':noticias,"secoes":secoes,'usuario_logado':usuario_logado})
