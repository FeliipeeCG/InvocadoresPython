from django.urls import path
from AppInvocador.views import lobby, grieta, lolero, coach, partida, setInvocador, getInvocador, buscarInvocador

urlpatterns = [
    path('lobby/', lobby, name="lobby"),
    path('grieta/', grieta, name="grieta"),
    path('lolero/', lolero, name="lolero"),
    path('coach/', coach, name="coach"),
    path('partida/', partida, name="partida"),
    path('setInvocador/', setInvocador, name="setInvocador"),
    path('getInvocador/', getInvocador, name="getInvocador"),
    path('buscarInvocador/', buscarInvocador, name="buscarInvocador"),
]
