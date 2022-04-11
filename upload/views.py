
import os
from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from noticias.views import noticias
from secao.models import Secao
from subsecao.models import Subsecao
from django.contrib import messages
from upload.models import Arquivo
from usuario.models import Usuario
from subsecao.models import Subsecao
from noticias.models import Noticia
from defesa.models import Defesa

# Define que tipos de arquivos nossa aplicação aceita

def upload(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    if(usuario_logado.permissao == 1):
        
        arquivos = Arquivo.objects.filter(usuario=usuario_logado)

    else:

        arquivos = Arquivo.objects.all()

    dados = []

    for arquivo in arquivos:

        subs = Subsecao.objects.filter(conteudo__icontains=arquivo.url)
        defesas = Defesa.objects.filter(conteudo__icontains= arquivo.url)
        noticias = list(Noticia.objects.filter(conteudo__icontains=arquivo.url))
        noticias.extend(list(Noticia.objects.filter(img=arquivo)))
        

        dado = {"arquivo":arquivo,"subsecoes":subs,"defesas":defesas,"noticias":noticias}

        dados.append(dado)

    return render(request,'upload/index.html',{'arquivos':dados,
                                                "secoes":secoes,
                                                "usuario_logado":usuario_logado,
                                                "subsecoes":subsecoes  
                                              })
   


def salvar_arquivo(request):


    try:

        arquivo = str(request.FILES['arquivo'])

    except :

        messages.add_message(request,messages.WARNING,"É necessário selecionar um arquivo")
        return redirect('/upload/')


    arquivo = str(request.FILES['arquivo']).split('.')
    nomeArquivo = arquivo[0]
    extensaoArquivo = arquivo[-1].lower()
    
    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))
    
 
    try:

        newdoc = Arquivo(nome = nomeArquivo, url = request.FILES['arquivo'],extensao = extensaoArquivo, usuario = usuario_logado)
        newdoc.save()
        messages.add_message(request,messages.SUCCESS,"Upload realizado com sucesso")

    except: 

        messages.add_message(request,messages.WARNING,"Ocorreu um erro ao salvar o arquivo")

   

    return redirect('/upload/')


def excluir_arquivo(request,id):

    try:
        

        arquivo = Arquivo.objects.filter(id=id).first()

        subs = Subsecao.objects.filter(conteudo__icontains=arquivo.url)
        defesas = Defesa.objects.filter(conteudo__icontains= arquivo.url)
        noti = list(Noticia.objects.filter(conteudo__icontains=arquivo.url))
        noti.extend(list(Noticia.objects.filter(img=arquivo)))

        if len(subs) > 0 or len(defesas) > 0 or len(noti) > 0:

            messages.add_message(request,messages.WARNING,"Arquivos está sendo utilizado")
            return redirect("/upload/")

        try:   

            os.unlink("./media/"+str(arquivo.url))

        except OSError:
             
            messages.add_message(request,messages.WARNING,"Arquivo não foi encontrado")
        
        try:
            
            arquivo.delete()
            messages.add_message(request,messages.SUCCESS,"Arquivo foi excluido com sucesso")

        except:

            messages.add_message(request,messages.WARNING,"Arquivo não pode ser excluido")

        return redirect('/upload/')
    
    except:

        return redirect('/upload/')


def excluir_tudo(request):

    try:
        
        arquivos = Arquivo.objects.all()
        
        i  = 0
        isUsado = False

        while i < len(arquivos):

            subs = Subsecao.objects.filter(conteudo__icontains=arquivos[i].url)
            defesas = Defesa.objects.filter(conteudo__icontains= arquivos[i].url)
            noti = list(Noticia.objects.filter(conteudo__icontains=arquivos[i].url))
            noti.extend(list(Noticia.objects.filter(img=arquivos[i])))

            if len(subs) == 0 and len(defesas) == 0 and len(noti) == 0:

                try: 
                
                    os.unlink("./media/"+str(arquivos[i].url))

                except OSError as e:
                    arquivos[i].delete()
                    i+=1
                    continue
                
                arquivos[i].delete()
               

            else:

                isUsado = True

            i+=1

        if isUsado:

            messages.add_message(request,messages.WARNING,"Alguns arquivos estão sendo utilizados")
            return redirect('/upload/')

        messages.add_message(request,messages.SUCCESS,"Arquivos excluidos com sucesso")
        return redirect('/upload/')
    
    except:

        messages.add_message(request,messages.WARNING,"Erro ao excluir alguns arquivos")

        return redirect('/upload/')



def buscarArquivo(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    if(request.method == 'POST'):

        chave = request.POST.get('valor_pesquisa')

        arquivos = Arquivo.objects.filter(nome__icontains=chave)

    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    return render(request,"upload/index.html",{'arquivos':arquivos,"secoes":secoes,'usuario_logado':usuario_logado,'subsecoes':subsecoes})


def buscarImagens(request):

    lista_extensao = ['JPEG','PNG','PDF','SVG','JPG']

    lista_imagens = []

    for extensao in lista_extensao:

        arquivos = Arquivo.objects.filter(extensao__icontains=extensao)

        for arq in arquivos:

            lista_imagens.append({"id":arq.id,"nome":arq.nome, "url": str(arq.url)})


    return JsonResponse(lista_imagens,safe=False)
