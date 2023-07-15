from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppInvocador.models import invocador
from AppInvocador.forms import formSetInvocador
# Create your views here.


def lobby(request):
    return render(request, "AppInvocador/lobby.html")


def grieta(request):
    return render(request, "AppInvocador/grieta.html")


def lolero(request):
    Invocadores = invocador.objects.all()
    return render(request, "AppInvocador/lolero.html", {"Invocadores": Invocadores})


def coach(request):
    return render(request, "AppInvocador/coach.html")


def partida(request):
    return render(request, "AppInvocador/partida.html")


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


def getInvocador(request):
    return render(request, "AppInvocador/getInvocador.html")


def buscarInvocador(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        invocadores = invocador.objects.filter(nombre=nombre)
        return render(request, "AppInvocador/getInvocador.html", {"invocadores": invocadores})
    else:
        return render(request, "AppInvocador/errorInvocador.html")

    return HttpResponse(respuesta)


def eliminarInvocador(request, nombre_invocador):
    Invocador = invocador.objects.get(nombre=nombre_invocador)
    Invocador.delete()
    miFormulario = formSetInvocador()
    Invocadores = invocador.objects.all()
    return render(request, "AppInvocador/setInvocador.html", {"miFormulario": miFormulario, "Invocador": Invocador})


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
