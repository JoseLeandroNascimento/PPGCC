
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


    
    try:

        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

        if usuario_logado.permissao == 2:

            secoes = Secao.objects.all().order_by('ordem')
            noticias = Noticia.objects.all()
            subsecoes = Subsecao.objects.all().order_by('ordem')

        else:

            secoes = Secao.objects.filter(usuarios = usuario_logado).order_by('ordem')
            noticias = Noticia.objects.filter(usuario=usuario_logado)
            subsecoes = Subsecao.objects.all().order_by('ordem')

    except:

        messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
        return redirect("/login/")

    return render(request, "noticias/index.html", {"noticias": noticias, "secoes": secoes, 'usuario_logado': usuario_logado,'subsecoes':subsecoes})


def add_noticia(request):

    
    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')
    
    try:

        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

        if usuario_logado.permissao == 2:

            secoes = Secao.objects.all().order_by('ordem')
           
            subsecoes = Subsecao.objects.all().order_by('ordem')

        else:

            secoes = Secao.objects.filter(usuarios = usuario_logado).order_by('ordem')
            subsecoes = Subsecao.objects.all().order_by('ordem')


    except:

        messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
        return redirect("/login/")

    return render(request, "noticias/add_noticia.html", {"subsecoes":subsecoes,"secoes": secoes, 'usuario_logado': usuario_logado})


def salvar_noticia(request):

    if(request.method == "POST"):

        titulo = request.POST.get("titulo")
        previa = request.POST.get("previa")
        conteudo = request.POST.get("conteudo")
        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        # Esse try verifica se ocorreu tudo certo com o upload do arquivo ou se o usuário selecionou algum
        try:

            arquivo = str(request.FILES['arquivo_upload'])
        
        except:

            messages.add_message(request,messages.WARNING,"É necessário selecionar um arquivo")
            return redirect('/add_noticia/')

       
        arquivo = str(request.FILES['arquivo_upload']).split('.')
        nomeArquivo = arquivo[0]
        extensaoArquivo = arquivo[-1].lower()
        
        try:
            

            newdoc = Arquivo(nome = nomeArquivo, url = request.FILES['arquivo_upload'],extensao = extensaoArquivo, usuario = usuario_logado)
            newdoc.save()
            img = newdoc

        except:

            messages.add_message(request,messages.WARNING,"Ocorreu um erro ao salvar o arquivo")
            return redirect('/add_noticia/')

       
        novaNoticia = Noticia(titulo= titulo, previa = previa, conteudo=conteudo, img= img, usuario = usuario_logado)
        
        try:
            
            novaNoticia.save()
            messages.add_message(request,messages.SUCCESS,"Notícia publicada com sucesso")

        except IntegrityError:

            messages.add_message(request, messages.WARNING,"Ocorreu um erro ao publicar a notícia")
            return redirect('/noticias/')



    return redirect("/noticias/")


def excluir_noticia(request):

    if(request.method == "POST"):
        
        try:
            
            id = request.POST.get("id_noticia")
            noticia = Noticia.objects.filter(id=id).first()
            noticia.delete()
            messages.add_message(request, messages.SUCCESS,"Notícia deletada com sucesso")

        
        except IntegrityError:
            
            messages.add_message(request, messages.WARNING,"Noticia não pode ser deletada")


    return redirect("/noticias/")


def editar_noticia(request):

    

    if(request.method == "POST"):


        try:

            id = request.POST.get("id_noticia")
            noticia = Noticia.objects.filter(id=id).first()
            usuario_logado = Usuario.objects.get(
                id=request.session.get('id_usuario'))

            if usuario_logado.permissao == 2:

                secoes = Secao.objects.all().order_by('ordem')
                subsecoes = Subsecao.objects.all().order_by('ordem')

            else:

                secoes = Secao.objects.filter(usuario=usuario_logado).order_by('ordem')
                subsecoes = Subsecao.objects.all().order_by('ordem')

        except:

            messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
            return redirect("/login/")

        return render(request, "noticias/editar_noticia.html", {"noticia": noticia, "secoes":secoes,'usuario_logado':usuario_logado,"subsecoes":subsecoes})


def update_noticia(request):

    if(request.method == "POST"):
        id_noticia = request.POST.get("id_noticia")
        titulo = request.POST.get("titulo")
        previa = request.POST.get("previa")
        conteudo = request.POST.get("conteudo")
        id_usuario = request.POST.get("id_usuario")
      
        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        try:

            arquivo = str(request.FILES['arquivo_upload'])

            arquivo = str(request.FILES['arquivo_upload']).split('.')
            nomeArquivo = arquivo[0]
            extensaoArquivo = arquivo[-1].lower()
            
            try:
                

                newdoc = Arquivo(nome = nomeArquivo, url = request.FILES['arquivo_upload'],extensao = extensaoArquivo, usuario = usuario_logado)
                newdoc.save()
                img = newdoc

            except:

                messages.add_message(request,messages.WARNING,"Ocorreu um erro ao salvar o arquivo")
                return redirect('/add_noticia/')
        except:


            img = Noticia.objects.get(id=id_noticia).img

       
        

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

    

    if(request.method == 'POST'):

        valor_pesquisa = request.POST.get('valor_pesquisa')

        

        try:

            usuario_logado = Usuario.objects.get(
                id=request.session.get('id_usuario'))

            if usuario_logado.permissao == 2:

                secoes = Secao.objects.all().order_by('ordem')
                subsecoes = Subsecao.objects.all().order_by('ordem')
                noticias = Noticia.objects.all().filter(titulo__icontains=valor_pesquisa)

            else:

                secoes = Secao.objects.filter(usuario=usuario_logado).order_by('ordem')
                subsecoes = Subsecao.objects.all().order_by('ordem')
                noticias = Noticia.objects.all().filter(titulo__icontains=valor_pesquisa).filter(usuario=usuario_logado)

        except:

            usuario_logado = None

    return render(request, "noticias/index.html", {'noticias':noticias,"secoes":secoes,'usuario_logado':usuario_logado,"subsecoes":subsecoes})
