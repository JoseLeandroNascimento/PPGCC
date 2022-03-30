from re import sub
from django.db import IntegrityError
from django.shortcuts import redirect, render
from secao.models import Secao
from subsecao.models import Subsecao
from usuario.models import Usuario


def cadastroSubsecao(request, id_secao):

    secao = Secao.objects.get(id=id_secao)
    subsecoes = Subsecao.objects.filter(secao=secao)
    cont_subsecoes = list(range(1, len(subsecoes)+2))
    max_ordem = len(subsecoes)+1
    usuario_logado = request.session.get('id_usuario')
    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')

    return render(request, 'subsecao/index.html', {"id_secao": id_secao, "subsecoes": subsecoes, "cont_subsecoes": cont_subsecoes, "max_ordem": max_ordem, "usuario_logado": usuario_logado, "secoes": secoes, "subsecoes": subsecoes})


def salvarSubsecao(request):

    if(request.method == 'POST'):

        titulo = request.POST.get('titulo')
        ordem = request.POST.get('ordem')
        ativa = request.POST.get('ativada')
        id_usuario = request.POST.get('id_usuario')
        id_secao = request.POST.get('id_secao')

        usuario = Usuario.objects.get(id=id_usuario)
        secao = Secao.objects.get(id=id_secao)

        subsecoes = Subsecao.objects.filter(secao=secao).order_by('ordem')

        for sub in subsecoes:

            if sub.ordem >= int(ordem):

                sub.ordem = sub.ordem + 1
                sub.save()

        novaSubsecao = Subsecao(titulo=titulo, ordem=ordem, ativo=ativa, secao=secao, usuarios=usuario)

        try:

            novaSubsecao.save()

        except IntegrityError:

            return redirect('/home/')

        return redirect('/subsecao-view/'+str(novaSubsecao.id))


def subsecao(request, id_subsecao):

    sub = Subsecao.objects.get(id=id_subsecao)
    subsecoes = Subsecao.objects.all().order_by('ordem')
    conteudo = sub.conteudo
    secoes = Secao.objects.all().order_by('ordem')

    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    return render(request, 'subsecao/view.html', {

        "conteudo": conteudo,
        "subsecao": sub,
        'subsecoes': subsecoes,
        'secoes': secoes,
        'usuario_logado': usuario_logado
    })


def subsecaoEditar(request):

    if request.method == 'POST':

        sub = Subsecao.objects.get(id=request.POST.get('subsecao'))
        secoes = Secao.objects.all().order_by('ordem')
        subsecoes = Subsecao.objects.all().order_by('ordem')
        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))

        return render(request, 'subsecao/editar.html', {
            'subsecao': sub,
            'secoes': secoes,
            'subsecoes': subsecoes,
            'usuario_logado': usuario_logado

        })


def configurar(request):

    if(request.method == 'POST'):

        subsecao = Subsecao.objects.get(id=request.POST.get('id_subsecao'))

        subsecoes = Subsecao.objects.filter(secao=subsecao.secao)
        cont_subsecoes = list(range(1, len(subsecoes)+1))
        max_ordem = len(subsecoes)
        usuario_logado = Usuario.objects.get(
            id=request.session.get('id_usuario'))
        secoes = Secao.objects.all().order_by('ordem')
        subsecoes = Subsecao.objects.filter(
            secao=subsecao.secao).order_by('ordem')

        return render(request, 'subsecao/configurar.html', {
            "subsecoes": subsecoes,
            "cont_subsecoes": cont_subsecoes,
            "max_ordem": max_ordem,
            "usuario_logado": usuario_logado,
            "secoes": secoes,
            'subsecao': subsecao,
            "id_secao": subsecao.secao.id
        })


def updateSubsecao(request):

    if(request.method == 'POST'):

        subsecaoDados = request.POST

        titulo = subsecaoDados.get('titulo')
        ordem = subsecaoDados.get('ordem')
        ativada = subsecaoDados.get('ativada')
        id_subsecao = subsecaoDados.get('id_subsecao')

        subsecao = Subsecao.objects.get(id=id_subsecao)

        subsecao.titulo = titulo
        subsecao.ativo = ativada

        try:

            subsecao.save()

        except IntegrityError:

            return redirect('/subsecao-view/'+str(subsecao.id))

        ordem_atual = subsecao.ordem

        subsecoes = Subsecao.objects.filter(
            secao=subsecao.secao).order_by('ordem')

        ordem_destino = int(ordem)

        lista_aux = []

        for sec in subsecoes:

            dados = [sec.id, sec.ordem, sec.titulo]
            lista_aux.append(dados)

        for sec in lista_aux:

            # Quando a seção for para uma ordem maior do que atual

            if ordem_destino > ordem_atual:

                if sec[1] == ordem_atual:

                    sec[1] = ordem_destino

                else:

                    if sec[1] == ordem_destino:

                        sec[1] = sec[1] - 1
                        break

                    if sec[1] > ordem_atual:

                        sec[1] = sec[1] - 1

            elif ordem_destino < ordem_atual:

                if sec[1] == ordem_atual:

                    sec[1] = ordem_destino
                    break

                if sec[1] >= ordem_destino:

                    sec[1] = sec[1] + 1

        for sec in lista_aux:

            subsecao_update = Subsecao.objects.get(id=sec[0])
            subsecao_update.ordem = sec[1]
            subsecao_update.save()

        return redirect('/subsecao-view/'+str(subsecao.id))


def atualizarSubsecao(request):

    if(request.method == 'POST'):

        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        id_subsecao = request.POST.get('id_subsecao')

        subsecao = Subsecao.objects.get(id=id_subsecao)

        subsecao.titulo = titulo
        subsecao.conteudo = conteudo

        try:

            subsecao.save()

        except IntegrityError:

            return redirect('/subsecao-view/'+str(subsecao.id))

        return redirect('/subsecao-view/'+str(subsecao.id))


def delete(request):

    if(request.method == 'POST'):

        subsecao = Subsecao.objects.get(id=request.POST.get('id_subsecao'))
        ordem = subsecao.ordem
        subsecoes = Subsecao.objects.filter(secao=subsecao.secao)

        subsecao.delete()

        for sub in subsecoes:

            if sub.ordem > ordem:

                sub.ordem = sub.ordem - 1
                sub.save()

        return redirect('/home/')


def subsecaoClear(request):

    if request.method == 'POST':

        subsecao = Subsecao.objects.get(id=request.POST.get('id_subsecao'))

        subsecao.conteudo = ''
        subsecao.save()

        return redirect('/subsecao-view/'+str(subsecao.id))
