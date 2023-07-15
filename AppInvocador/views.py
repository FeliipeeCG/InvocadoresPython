from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppInvocador.models import invocador
from AppInvocador.forms import formSetInvocador
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def lobby(request):
    return render(request, "AppInvocador/lobby.html")


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
