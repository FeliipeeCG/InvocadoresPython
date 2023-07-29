from django.urls import path
from django.contrib.auth.views import LogoutView
from AppInvocador.views import *

urlpatterns = [
    path('', loginApp),
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
    path('login/', loginApp, name="login"),
    path('registro/', registro, name="registro"),
    path('Logout/', LogoutView.as_view(template_name='AppInvocador/login.html'), name="Logout"),
    path('perfil/', perfilview, name="perfil"),
    path('Perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('Perfil/changePassword/', changePassword, name="changePassword"),
    path('Perfil/changeAvatar/', editAvatar, name="editAvatar"),]
