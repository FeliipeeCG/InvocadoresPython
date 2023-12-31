from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class invocador(models.Model):
    nombre = models.CharField(max_length=30)
    nick = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"nombre: {self.nombre} / nick: {self.nick} / email: {self.email} "


class coach(models.Model):
    nombre = models.CharField(max_length=30)
    nick = models.CharField(max_length=30)
    email = models.EmailField()
    equipo = models.CharField(max_length=30)

    def __str__(self):
        return f"nombre: {self.nombre} - nick: {self.nick} - equipo: {self.equipo} "


class partida(models.Model):
    tipo = models.CharField(max_length=30)
    fechaJugada = models.DateField()
    entregada = models.BooleanField()

    def __str__(self):
        return f"Tipo: {self.tipo} - Fecha: {self.fechaJugada}  "


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)
