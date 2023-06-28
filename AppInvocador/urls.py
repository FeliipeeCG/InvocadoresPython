from django.urls import path
from AppInvocador.views import lobby, grieta, invocador, coach, partida
urlpatterns = [
    path('lobby/', lobby, name="lobby"),
    path('grieta/', grieta, name="grieta"),
    path('invocador/', invocador, name="invocador"),
    path('coach/', coach, name="coach"),
    path('partida/', partida, name="partida"),
]
