from django.shortcuts import redirect, render
from secao.models import Secao
from subsecao.models import Subsecao
from usuario.models import Usuario
from django.contrib import messages

def home(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    try:


        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        if usuario_logado.permissao == 2:

            secoes = Secao.objects.all().order_by('ordem')
            subsecoes = Subsecao.objects.all().order_by('ordem')

        else:

            secoes = Secao.objects.filter(usuarios = usuario_logado).order_by('ordem')
            subsecoes = Subsecao.objects.all().order_by('ordem')
    except:

        messages.add_message(request,messages.WARNING,"É necessário autenticação")
        return redirect("/login/") 


    
    return render(request,'index.html',{'secoes':secoes,'usuario_logado':usuario_logado,'subsecoes':subsecoes}
)