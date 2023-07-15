from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from AppInvocador.models import invocador, Avatar
from AppInvocador.forms import formSetInvocador, UserEditForm, ChangePasswordForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


@login_required
def lobby(request):
    avatar = getavatar(request)
    return render(request, "AppInvocador/lobby.html", {"avatar": avatar})


@login_required
def grieta(request):
    return render(request, "AppInvocador/grieta.html")


@login_required
def lolero(request):
    Invocadores = invocador.objects.all()
    return render(request, "AppInvocador/lolero.html", {"Invocadores": Invocadores})


@login_required
def coach(request):
    return render(request, "AppInvocador/coach.html")


@login_required
def partida(request):
    return render(request, "AppInvocador/partida.html")


@login_required
def setInvocador(request):
    if request.method == 'POST':
        miFormulario = formSetInvocador(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            Invocador = invocador(
                nombre=data["nombre"], nick=data["nick"], email=data["email"])
            Invocador.save()
            return render(request, "AppInvocador/nuevoInvocador.html")
    else:
        miFormulario = formSetInvocador()
    return render(request, "AppInvocador/setInvocador.html", {"miFormulario": miFormulario})


@login_required
def getInvocador(request):
    return render(request, "AppInvocador/getInvocador.html")


@login_required
def buscarInvocador(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        invocadores = invocador.objects.filter(nombre=nombre)
        return render(request, "AppInvocador/getInvocador.html", {"invocadores": invocadores})
    else:
        return render(request, "AppInvocador/errorInvocador.html")

    return HttpResponse(respuesta)


@login_required
def eliminarInvocador(request, nombre_invocador):
    Invocador = invocador.objects.get(nombre=nombre_invocador)
    Invocador.delete()
    miFormulario = formSetInvocador()
    Invocadores = invocador.objects.all()
    return render(request, "AppInvocador/setInvocador.html", {"miFormulario": miFormulario, "Invocador": Invocador})


@login_required
def editarInvocador(request, nombre_invocador):
    Invocador = invocador.objects.get(nombre=nombre_invocador)
    if request.method == 'POST':
        miFormulario = formSetInvocador(request.POST)
        if miFormulario.is_valid:
            print(miFormulario)
            data = miFormulario.cleaned_data
            Invocador.nombre = data['nombre']
            Invocador.nick = data['nick']
            Invocador.email = data['email']
            Invocador.save()
            miFormulario = formSetInvocador()
            Invocadores = invocador.objects.all()
            return render(request, "AppInvocador/setInvocador.html", {"miFormulario": miFormulario, "Invocador": Invocador})
    else:
        miFormulario = formSetInvocador(initial={
                                        'nombre': invocador.nombre, 'nick': invocador.nick, 'email': invocador.email})
    return render(request, "AppInvocador/editarInvocador.html", {"miFormulario": miFormulario})


def loginApp(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['user'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, "AppInvocador/lobby.html")
        else:
            return render(request, "AppInvocador/login.html", {'error': 'Usuario o contraseña incorrecta'})
    else:
        return render(request, "AppInvocador/login.html")


def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request, 'AppInvocador/login.html')
    else:
        return render(request, 'AppInvocador/registro.html')


@login_required
def perfilview(request):
    return render(request, 'AppInvocador/Perfil/perfil.html')


@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id=usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'AppInvocador/Perfil/perfil.html')
    else:
        form = UserEditForm(initial={'username': usuario.username, 'email': usuario.email,
                            'first_name': usuario.first_name, 'last_name': usuario.last_name})
        return render(request, 'AppInvocador/Perfil/editarPerfil.html', {"form": form})


@login_required
def changePassword(request):
    usuario = request.user
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse("Las constraseñas no coinciden")
        return render(request, "AppInvocador/lobby.html")
    else:
        form = ChangePasswordForm(user=usuario)
        return render(request, 'AppInvocador/Perfil/changePassword.html', {"form": form})


def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username=request.user)
            avatar = Avatar(
                user=user, image=form.cleaned_data['avatar'], id=request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user=request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, "AppCoder/lobby.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user=request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "AppInvocador/Perfil/avatar.html", {'form': form})


def getavatar(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar
