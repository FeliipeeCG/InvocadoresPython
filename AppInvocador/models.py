from django.db import models

# Create your models here.


class invocador(models.Model):
    nombre = models.CharField(max_length=30)
    nick = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"nombre: {self.nombre} - nick: {self.nick} - email: {self.email} "


class coach(models.Model):
    nombre = models.CharField(max_length=30)
    nick = models.CharField(max_length=30)
    email = models.EmailField()
    equipo = models.CharField(max_length=30)


class partida(models.Model):
    tipo = models.CharField(max_length=30)
    fechaJugada = models.DateField()
    entregada = models.BooleanField()
