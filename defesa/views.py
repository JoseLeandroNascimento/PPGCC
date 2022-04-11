
from email import message
from os import sep
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.db.models import Q
from defesa.models import Defesa
from secao.models import Secao
from subsecao.models import Subsecao
from usuario.models import Usuario
from django.contrib import messages


def defesa(request):


    try:

        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        if usuario_logado.permissao == 2:

            defesas = Defesa.objects.all()
            secoes = Secao.objects.all().order_by('ordem')
            subsecoes = Subsecao.objects.all().order_by('ordem')

        else:

            defesas = Defesa.objects.filter(usuario=usuario_logado)
            secoes = Secao.objects.filter(usuario= usuario_logado).order_by('ordem')
            subsecoes = Subsecao.objects.filter(usuarios=usuario_logado).order_by('ordem')
    except:

        messages.add_message(request,messages.WARNING,"É necessário autenticação")
        return redirect("/login/") 

   

    return render(request, 'defesa/index.html', {
        'defesas': defesas,
        "secoes": secoes,
        'usuario_logado': usuario_logado,
        "subsecoes": subsecoes
    })




def cadatroDefesa(request):

    

    try:

        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        if usuario_logado.permissao == 2:

            secoes = Secao.objects.all().order_by('ordem')
            subsecoes = Subsecao.objects.all().order_by('ordem')

        else:

            secoes = Secao.objects.filter(usuario= usuario_logado).order_by('ordem')
            subsecoes = Subsecao.objects.filter(usuarios=usuario_logado).order_by('ordem')

    except:

        messages.add_message(request,messages.WARNING,"É necessário autenticação")
        return redirect("/login/")
    return render(request, "defesa/cadastroDefesa.html", {"secoes": secoes, 'usuario_logado': usuario_logado, "subsecoes": subsecoes})




def salvarDefesa(request):

    if(request.method == 'POST'):

        dados = request.POST
        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))
        titulo = dados.get('titulo')
        local = dados.get('local')
        horario = dados.get('horario')
        conteudo = dados.get('conteudo')

        try:

            novaDefesa = Defesa(titulo=titulo, local=local, horario=horario,
                                conteudo=conteudo, usuario=usuario_logado)
            novaDefesa.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Defesa criada com sucesso")

        except IntegrityError:

            if (Defesa.objects.get(titulo=titulo)):

                secoes = Secao.objects.all().order_by('ordem')
                usuario_logado = Usuario.objects.get(
                    id=request.session.get('id_usuario'))
                subsecoes = Subsecao.objects.all().order_by('ordem')

                messages.add_message(
                    request, messages.WARNING, "Já existe um defesa com mesmo titulo cadastrada no sistema")
                return render(request, "defesa/cadastroDefesa.html", {
                    "secoes": secoes,
                    'usuario_logado': usuario_logado,
                    "subsecoes": subsecoes,
                    "titulo": titulo,
                    "local": local,
                    "horario": horario,
                    "conteudo": conteudo
                })

            else:

                messages.add_message(
                    request, messages.WARNING, "Notícia não pode ser criada")

    return redirect('/defesa/')





def excluirDefesa(request):

    if(request.method == 'POST'):

        id = request.POST.get('id_defesa')

        defesa = Defesa.objects.filter(id=id).first()

        try:

            defesa.delete()
            messages.add_message(request, messages.SUCCESS,
                                 "Defesa deletada com sucesso")

        except IntegrityError:

            messages.add_message(request, messages.WARNING,
                                 "Não foi possível deletar defesa")

    return redirect("/defesa/")






def buscarDefesas(request):

   

    if request.method == 'POST':

        try:
            
            usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

            if usuario_logado.permissao == 2:

                secoes = Secao.objects.all().order_by('ordem')
                subsecoes = Subsecao.objects.all().order_by('ordem')

            else:

                secoes = Secao.objects.filter(usuarios=usuario_logado).order_by('ordem')
                subsecoes = Subsecao.objects.all().order_by('ordem')
        except:

            messages.add_message(request,messages.WARNING,"É necessário autenticação")
            return redirect("/login/")

        valor_pesquisa = request.POST.get('valor_pesquisa')

        defesas = Defesa.objects.filter(Q(titulo__icontains=valor_pesquisa) | Q(local__icontains=valor_pesquisa)).filter(usuario=usuario_logado)


    return render(request, 'defesa/index.html', {'defesas': defesas, "secoes": secoes, 'usuario_logado': usuario_logado, "subsecoes": subsecoes})







def editarDefesa(request):

    

    if(request.method == 'POST'):

        try:

            usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

            if usuario_logado.permissao == 2:

                secoes = Secao.objects.all().order_by('ordem')
                subsecoes = Subsecao.objects.all().order_by('ordem')

            else:

                secoes = Secao.objects.filter(usuarios=usuario_logado).order_by('ordem')
                subsecoes = Subsecao.objects.all().order_by('ordem')

        except:

            messages.add_message(request, messages.WARNING,"É necessário autenticação")
            return redirect("/login/")


        defesa_id = request.POST.get('defesa_id')

        defesa = Defesa.objects.get(id=defesa_id)


    return render(request, "defesa/editarDefesa.html", {'defesa': defesa, "secoes": secoes, 'usuario_logado': usuario_logado, "subsecoes": subsecoes})






def updateDefesa(request):

    if(request.method == 'POST'):

        dados = request.POST

        titulo = dados.get('titulo')
        local = dados.get('local')
        horario = dados.get('horario')
        conteudo = dados.get('conteudo')

        try:

            usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        except:

            messages.add_message(request,messages.WARNING,"É necessário autenticação")
            return redirect("/login/")

        id_defesa = dados.get('id_defesa')

        defesa = Defesa.objects.filter(id=id_defesa).first()

        if(defesa):

            defesa.titulo = titulo
            defesa.local = local
            defesa.horario = horario
            defesa.conteudo = conteudo
            defesa.usuario = usuario_logado

            try:

                defesa.save()

                messages.add_message(
                    request, messages.SUCCESS, "Defesa foi editada com sucesso")

            except IntegrityError:

                if (Defesa.objects.get(titulo=titulo)):

                    secoes = Secao.objects.all().order_by('ordem')
                    usuario_logado = Usuario.objects.get(
                        id=request.session.get('id_usuario'))
                    subsecoes = Subsecao.objects.all().order_by('ordem')

                    messages.add_message(
                        request, messages.WARNING, "Já existe uma defesa com mesmo título cadastrada no sistema")
                    return render(request, "defesa/cadastroDefesa.html", {
                        "secoes": secoes,
                        'usuario_logado': usuario_logado,
                        "subsecoes": subsecoes,
                        "titulo": titulo,
                        "local": local,
                        "horario": horario,
                        "conteudo": conteudo
                    })

                else:

                    messages.add_message(
                        request, messages.WARNING, "Defesa não pode ser editada")

            defesa.save()

    return redirect('/defesa/')
