from django.shortcuts import render
from secao.models import Secao
from subsecao.models import Subsecao
from usuario.models import Usuario


def home(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    return render(request,'index.html',{'secoes':secoes,'usuario_logado':usuario_logado,'subsecoes':subsecoes}
)