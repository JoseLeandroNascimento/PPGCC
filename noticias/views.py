
from unittest import result
from django.db import IntegrityError
from django.shortcuts import redirect, render
from noticias.models import Noticia
from secao.models import Secao
from subsecao.models import Subsecao
from usuario.models import Usuario
from upload.models import Arquivo
from django.contrib import messages




def noticias(request):

    secoes = Secao.objects.all().order_by('ordem')
    noticias = Noticia.objects.all()
    subsecoes = Subsecao.objects.all().order_by('ordem')
    
    try:

        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

    except:

        usuario_logado = None

    return render(request, "noticias/index.html", {"noticias": noticias, "secoes": secoes, 'usuario_logado': usuario_logado,'subsecoes':subsecoes})


def add_noticia(request):

    lista_imagens = ['JPEG','PNG','PDF','SVG']
    
    secoes = Secao.objects.all().order_by('ordem')

    imagens = []
    for tipo in lista_imagens:

        result = Arquivo.objects.filter(extensao__icontains=tipo)
        print(result)
        if result:
            imagens.extend(list(result))

    subsecoes = Subsecao.objects.all().order_by('ordem')
    
    try:

        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

    except:

        usuario_logado = None

    return render(request, "noticias/add_noticia.html", {"subsecoes":subsecoes,"secoes": secoes, 'usuario_logado': usuario_logado, 'imagens': imagens})


def salvar_noticia(request):

    if(request.method == "POST"):

        titulo = request.POST.get("titulo")
        previa = request.POST.get("previa")
        conteudo = request.POST.get("conteudo")
        img_id = request.POST.get('img_id')
        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        try:

            arquivo = str(request.FILES['arquivo_upload'])

            arquivo = str(request.POST.get('arquivo_upload')).split('.')
            nomeArquivo = arquivo[0]
            extensaoArquivo = arquivo[-1].lower()
            
            try:

                newdoc = Arquivo(nome = nomeArquivo, url = request.POST.get('arquivo_upload'),extensao = extensaoArquivo, usuario = usuario_logado)
                newdoc.save()
                messages.add_message(request,messages.SUCCESS,"Upload realizado com sucesso")

            except: 

                messages.add_message(request,messages.WARNING,"Ocorreu um erro ao salvar o arquivo")

        except :

            messages.add_message(request,messages.WARNING,"É necessário selecionar um arquivo")
            return redirect('/add_noticia/')

      

        

    
        if(img_id == '-1' or img_id == ''):

            messages.add_message(request, messages.WARNING,"É necessário fornecer uma imagem")
            return redirect("/noticias/")

        else:

            img = Arquivo.objects.get(id = img_id )

            try:
                                
                usuario = Usuario.objects.get(
                id=request.session.get('id_usuario'))
                messages.add_message(request,messages.SUCCESS,"Notícia publicada com sucesso")
            except:

                usuario = None

            novaNoticia = Noticia(titulo= titulo, previa = previa, conteudo=conteudo, img= img, usuario = usuario)

            try:
                novaNoticia.save()

            except IntegrityError:

                messages.add_message(request, messages.WARNING,
                """Houve um erro ao tentar salvar a noticia, o motivo pode ser um desses:
                    <ul>
                        <li>Não foi informado uma imagem</li>
                    </ul>
                """)



    return redirect("/noticias/")


def excluir_noticia(request):

    if(request.method == "POST"):
        
        try:
            
            id = request.POST.get("id_noticia")
            noticia = Noticia.objects.filter(id=id).first()
            noticia.delete()
            messages.add_message(request, messages.WARNING,"Notícia deletada com sucesso")

        
        except IntegrityError:
            
            messages.add_message(request, messages.ERROR,"Noticia não pode ser deletada")


    return redirect("/noticias/")


def editar_noticia(request):

    secoes = Secao.objects.all().order_by('ordem')
    imagens = Arquivo.objects.filter(tipo_arquivo = 'imagem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    if(request.method == "POST"):



        try:

            id = request.POST.get("id_noticia")
            noticia = Noticia.objects.filter(id=id).first()
            usuario_logado = Usuario.objects.get(
                id=request.session.get('id_usuario'))

        except:

            usuario_logado = None

        return render(request, "noticias/editar_noticia.html", {"noticia": noticia, "secoes":secoes,'usuario_logado':usuario_logado,'imagens':imagens,"subsecoes":subsecoes})


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

        try:
            
            noticia.save()
            messages.add_message(request,messages.SUCCESS,"Notícia editada com sucesso")

        except IntegrityError:

            messages.add_message(request,messages.ERROR,"Não foi possivel editar a notícia")
            
    return redirect("/noticias/")


def buscarNoticia(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    if(request.method == 'POST'):

        valor_pesquisa = request.POST.get('valor_pesquisa')

        noticias = Noticia.objects.all().filter(titulo__icontains=valor_pesquisa)

    try:

        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

    except:

        usuario_logado = None

    return render(request, "noticias/index.html", {'noticias':noticias,"secoes":secoes,'usuario_logado':usuario_logado,"subsecoes":subsecoes})
