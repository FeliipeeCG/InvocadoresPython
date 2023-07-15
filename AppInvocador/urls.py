from django.urls import path
from AppInvocador.views import *

urlpatterns = [
    path('lobby/', lobby, name="lobby"),
    path('grieta/', grieta, name="grieta"),
    path('lolero/', lolero, name="lolero"),
    path('coach/', coach, name="coach"),
    path('partida/', partida, name="partida"),
    path('setInvocador/', setInvocador, name="setInvocador"),
    path('getInvocador/', getInvocador, name="getInvocador"),
    path('buscarInvocador/', buscarInvocador, name="buscarInvocador"),
    path('eliminarInvocador/<nombre_invocador>',
         eliminarInvocador, name="eliminarInvocador"),
    path('editarInvocador/<nombre_invocador>',
         editarInvocador, name="editarInvocador"),
    path('editarInvocador/', editarInvocador, name="editarInvocador"),
]
