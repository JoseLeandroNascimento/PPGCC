from django.shortcuts import redirect, render
from usuario.models import Usuario


def login(request):

    if request.session.get('id_usuario'):

        return redirect('/home/')

        
    return render(request,'login/index.html')



def logar(request):


    if(request.method == 'POST'):

        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        usuarioValido = Usuario.objects.filter(usuario = usuario).filter(senha = senha).first()

        if(usuarioValido):

            request.session['id_usuario'] = usuarioValido.id

            return redirect('/home/')

        else:

            return redirect('/login/')
        

def logout(request):


    del request.session['id_usuario']


    return redirect('/login/')