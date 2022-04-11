
from xml.sax.handler import property_interning_dict
from django.shortcuts import redirect, render
from secao.models import Secao
from django.db.models import Q
from subsecao.models import Subsecao
from usuario.models import Usuario
from secao.models import Secao
from django.contrib import messages

# Create your views here.


def usuario(request):

    

    try:


        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        if usuario_logado.permissao == 2:

            secoes = Secao.objects.all().order_by('ordem')
            usuarios = Usuario.objects.all()
            subsecoes = Subsecao.objects.all().order_by('ordem')

        else:
            
            messages.add_message(request,messages.WARNING,"Usuário tem acesso a esse recurso")
            return redirect("/home/")

    except :

        messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
        return redirect("/home/")


    
    return render(request, "usuario/index.html", {"secoes": secoes, "usuarios": usuarios, 'usuario_logado': usuario_logado,'subsecoes':subsecoes})


def cadastro(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    try:


        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    except :

        messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
        return redirect("/home/")



    return render(request, "usuario/cadastro.html", {'secoes': secoes,'usuario_logado':usuario_logado,'subsecoes':subsecoes})




def criar_usuario(request):

    if request.method == "POST":

        try:


            usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

            if usuario_logado.permissao != 2:

                messages.add_message(request,messages.WARNING,"Usuário não tem acesso a esse recurso")
                return redirect("/home/")

        except :

            messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
            return redirect("/home/")

        usuario_data = dict(request.POST)

        usuario = usuario_data["usuario"][0]
        tipo_usuario = usuario_data["tipo_usuario"][0]
        status = usuario_data["status"][0]
        senha1 = usuario_data["senha1"][0]
        senha2 = usuario_data["senha2"][0]
        tipo_usuario = usuario_data["tipo_usuario"][0]

        if senha1 != senha2:

            return redirect('/cadastro_usuario/')

        novo_usuario = Usuario(usuario=usuario, senha=senha1,
                               ativado=status, permissao=tipo_usuario)

        novo_usuario.save()

        try:

            listaSecoes = usuario_data["lista[]"]
           
            for idSecao in listaSecoes:

                secao = Secao.objects.get(id=idSecao)

                secao.usuarios.add(novo_usuario)

        except KeyError:

            ...

    return redirect('/usuario/')




def excluirUsuario(request):

    if(request.method == 'POST'):

        id_usuario = request.POST.get('id_usuario')

        usuario = Usuario.objects.get(id=id_usuario)

        usuario.delete()

    return redirect('/usuario/')





def buscarUsuario(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    if(request.method == 'POST'):

        valor_pesquisa = request.POST.get('valor_pesquisa')

        usuarios = Usuario.objects.filter(Q(usuario__icontains=valor_pesquisa))

    try:


        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        if usuario_logado.permissao != 2:

            messages.add_message(request,messages.WARNING,"Usuário não tem acesso a esse recurso")
            return redirect("/home/")

    except :

        messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
        return redirect("/home/")

    return render(request, "usuario/index.html", {'usuarios': usuarios, "secoes": secoes,'usuario_logado':usuario_logado,'subsecoes':subsecoes})




def editarUsuario(request):

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    if request.method == 'POST':

        usuario_id = request.POST.get('usuario_id')

        usuario = Usuario.objects.get(id=usuario_id)

        secoes_permitidas = Secao.objects.filter(usuarios=usuario)

   
    try:


        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        if(usuario_logado.permissao != 2):

            messages.add_message(request,messages.WARNING,"Usuário não tem acesso a esse recurso")
            return redirect("/home/")

    except :

        messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
        return redirect("/home/")

    return render(request, "usuario/editarUsuario.html", {'secoes': secoes, 'usuario': usuario, "secoes_permitidas": secoes_permitidas,'usuario_logado':usuario_logado,'subsecoes':subsecoes})



def updateUsuario(request):

    if(request.method == 'POST'):

        usuario_data = dict(request.POST)

        usuario = usuario_data["usuario"][0]
        tipo_usuario = usuario_data["tipo_usuario"][0]
        status = usuario_data["status"][0]
        tipo_usuario = usuario_data["tipo_usuario"][0]
        id_usuario = usuario_data['id_usuario'][0]

        usuarioUpdate = Usuario.objects.get(id=id_usuario)

        usuarioUpdate.usuario = usuario
        usuarioUpdate.ativado = status
        usuarioUpdate.permissao = tipo_usuario

        for secoes in Secao.objects.filter(usuarios=usuarioUpdate):

            secoes.usuarios.remove(usuarioUpdate)

        try:

            listaSecoes = usuario_data["lista[]"]

            for idSecao in listaSecoes:

                secao = Secao.objects.get(id=idSecao)

                secao.usuarios.add(usuarioUpdate)

        except KeyError:

            ...

        usuarioUpdate.save()
        

    return redirect("/usuario/")
