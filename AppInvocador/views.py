from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.


def lobby(request):
    return render(request, "AppInvocador/lobby.html")


def grieta(request):
    return render(request, "AppInvocador/grieta.html")


def invocador(request):
    return render(request, "AppInvocador/invocador.html")


def coach(request):
    return render(request, "AppInvocador/coach.html")


def partida(request):
    return render(request, "AppInvocador/partida.html")
