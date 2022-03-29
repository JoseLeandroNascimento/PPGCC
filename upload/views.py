import os
from django.http import HttpResponse
from django.shortcuts import redirect, render
from secao.models import Secao
from subsecao.models import Subsecao

from upload.models import Arquivo
from usuario.models import Usuario




# Define que tipos de arquivos nossa aplicação aceita

extensoes_permitidas = {

    'imagens': [

        'png',
        'jpeg'
        'svg'
    ],
    'documentos': [

        'word',
        'docx',
        'pdf',
        'txt'
    ]
}





def upload(request):

    arquivos = Arquivo.objects.all()
    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    # usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    # return render(request,'upload/index.html',{'arquivos':arquivos,
    #                                             "secoes":secoes,
    #                                             "usuario_logado":usuario_logado  
    #                                           })
    return render(request,'upload/index.html',{'arquivos':arquivos,
                                                "secoes":secoes,
                                                "subsecoes":subsecoes
                                               
                                              })


def salvar_arquivo(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    arquivo = str(request.FILES['arquivo'])
    arquivo = str(request.FILES['arquivo']).split('.')
    nomeArquivo = arquivo[0]
    extensaoArquivo = arquivo[-1].lower()

    
    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))
    isSalvo = True


    if( extensaoArquivo in extensoes_permitidas.get('imagens')):
        
        tipo_arquivo = 'imagem'

       
    elif ( extensaoArquivo in extensoes_permitidas.get('documentos') ):

        tipo_arquivo = 'documento'

    else :

        tipo_arquivo = None



    
    if tipo_arquivo != None:

        newdoc = Arquivo(nome = nomeArquivo, url = request.FILES['arquivo'],extensao = extensaoArquivo,tipo_arquivo = tipo_arquivo)
        newdoc.save()

    else:

        isSalvo = False
      

    arquivos = Arquivo.objects.all()
        
    return render(request,'upload/index.html',{'arquivos':arquivos,
                                                    'isSalvo': isSalvo,
                                                    "secoes":secoes,
                                                    'usuario_logado':usuario_logado,
                                                    'subsecoes':subsecoes
                                                    })



def excluir_arquivo(request,id):

    try:
        
        arquivo = Arquivo.objects.filter(id=id).first()

        try:       
            os.unlink("./media/"+str(arquivo.url))

        except OSError as e:
             ...

        arquivo.delete()

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


