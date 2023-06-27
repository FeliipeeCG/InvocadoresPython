from django.urls import path
from AppInvocador.views import lobby, grieta, invocador, coach, partida
urlpatterns = [
    path('lobby/', lobby),
    path('grieta/', grieta),
    path('invocador/', invocador),
    path('coach/', coach),
    path('partida/', partida),
]
