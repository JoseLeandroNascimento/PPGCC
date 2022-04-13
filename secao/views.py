from email import message
from django.db import IntegrityError
from django.shortcuts import redirect, render
from secao.models import Secao
from secao.icons import icons
from subsecao.models import Subsecao
from usuario.models import Usuario
from django.contrib import messages

def addSecao(request):

   
    


    try:

        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))
        
        if usuario_logado.permissao != 2:

            messages.add_message(request,messages.WARNING,"Usuário não tem acesso a esse recurso")
            return redirect("/home/")
    
        secoes = Secao.objects.all().order_by('ordem')
        num_ordem = len(secoes)

        secoes = Secao.objects.all().order_by('ordem')


        subsecoes = Subsecao.objects.all().order_by('ordem')
        
        ordens = list(range(1, num_ordem+2))

    except IndexError:

        messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
        return redirect('/login/')
    icon_secao = list(icons.values())[0]
    icon_secao_chave = list(icons.keys())[0]

    return render(request, "secao/index.html", {"ordens": ordens,
                                                "num_ordem": num_ordem,
                                                "secoes": secoes,
                                                "icons": icons,
                                                "icon_secao": icon_secao,
                                                "icon_secao_chave": icon_secao_chave,
                                                "iconsKeys": icons.keys(),
                                                "iconsValues": icons.values(),
                                                "usuario_logado": usuario_logado,
                                                "subsecoes":subsecoes

                                                })


def salvarSecao(request):

    if(request.method == 'POST'):

        titulo = request.POST.get('titulo')
        ordem = request.POST.get('ordem')
        icon = request.POST.get('icon')
        ativada = request.POST.get('ativada')

        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))


        secoes = Secao.objects.all()

        for secao in secoes:

            if secao.ordem >= int(ordem):

                nova_posicao = secao.ordem + 1

                secao.ordem = nova_posicao

                secao.save()

        novaSecao = Secao(titulo=titulo, 
                          ordem=ordem,
                          icon=icon, 
                          ativada=ativada,
                          usuario=usuario_logado
                      )

        

        try:

            novaSecao.save()
            novaSecao.usuarios.add(usuario_logado)
            novaSecao.save()
            messages.add_message(request,messages.SUCCESS, "Seção criada com sucesso")

        except IntegrityError:
            
            if Secao.objects.filter(titulo = titulo):

                messages.add_message(request,messages.WARNING,"Já existe seção com mesmo nome")
                redirect('/home/')

        except:
            messages.add_message(request,messages.WARNING,"A seção não pode ser criada")
            redirect('/home/')

    return redirect('/home/')


def editarSecao(request, id):

    try:
        
        usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

        if usuario_logado.permissao != 2:
            messages.add_message(request,messages.WARNING, "Usuário não tem acesso a esse recurso")
            return redirect("/home/")

    except IndexError:

        messages.add_message(request,messages.WARNING,"Usuário não está autenticado")
        return redirect("/login/")

    secoes = Secao.objects.all().order_by('ordem')
    subsecoes = Subsecao.objects.all().order_by('ordem')
    num_ordem = len(secoes)
    ordens = list(range(1, num_ordem+1))

    secao = Secao.objects.get(id=id)

    usuario_logado = Usuario.objects.get(id=request.session.get('id_usuario'))

    return render(request, 'secao/editarSecao.html', {"ordens": ordens,
                                                      "num_ordem": num_ordem,
                                                      "secoes": secoes,
                                                      "icons": icons,
                                                      "icone_secao": secao.icon,
                                                      "iconsKeys": icons.keys(),
                                                      "iconsValues": icons.values(),
                                                      "usuario_logado": usuario_logado,
                                                      "secao": secao,
                                                      "subsecoes":subsecoes
                                                      })


def updateSecao(request):

    if(request.method == 'POST'):

        titulo = request.POST.get('titulo')
        ordem = request.POST.get('ordem')
        icon = request.POST.get('icon')
        ativada = request.POST.get('ativada')
        id_usuario = request.POST.get('id_usuario')
        id_secao = request.POST.get('id_secao')



        # Obtem a seção com o id
        secao = Secao.objects.get(id=id_secao)

        secao.titulo = titulo
        secao.icon = icon
        secao.ativada = ativada

        secao.save()
        # Obtem todas seções na ordem crescente
        secoes = Secao.objects.all().order_by('ordem')


        ordem_atual = int(secao.ordem)
        ordem_destino = int(ordem)

        
        lista_aux = []

        for sec in secoes:

            dados = [sec.id,sec.ordem,sec.titulo]
            lista_aux.append(dados)


        

        for sec in lista_aux:

            # Quando a seção for para uma ordem maior do que atual

            if ordem_destino > ordem_atual:

               
                if sec[1] == ordem_atual:

                   
                    sec[1]= ordem_destino
                    
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

                   sec[1] =  sec[1] + 1
                


        for sec in lista_aux:

            secao_update = Secao.objects.get(id=sec[0])
            secao_update.ordem = sec[1]
            secao_update.save()
            
          


        return redirect('/home')



def excluirSecao(request):

    print('asdasd')
    if(request.method == 'POST'):

        id = request.POST.get('id')
       
        secao = Secao.objects.get(id=id)
        ordem = secao.ordem

        secao.delete()

        secoes = Secao.objects.all()
        ordem = 1
        for secao in secoes:

           
            secao.ordem = ordem
            secao.save()

            ordem +=1


    return redirect('/home')


