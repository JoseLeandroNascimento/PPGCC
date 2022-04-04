
import os
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from secao.models import Secao
from subsecao.models import Subsecao
from django.contrib import messages
from upload.models import Arquivo
from usuario.models import Usuario




# Define que tipos de arquivos nossa aplicação aceita




def upload(request):

    arquivos = Arquivo.objects.all()
    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    return render(request,'upload/index.html',{'arquivos':arquivos,
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
        while i < len(arquivos):

            try: 

               
                os.unlink("./media/"+str(arquivos[i].url))

            except OSError as e:
                arquivos[i].delete()
                i+=1
                continue
            
            arquivos[i].delete()
            i+=1

        return redirect('/upload/')
    
    except:

        return redirect('/upload/')



def buscarArquivo(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    if(request.method == 'POST'):

        chave = request.POST.get('valor_pesquisa')

        arquivos = Arquivo.objects.filter(nome__icontains=chave)

    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    return render(request,"upload/index.html",{'arquivos':arquivos,"secoes":secoes,'usuario_logado':usuario_logado,'subsecoes':subsecoes})


