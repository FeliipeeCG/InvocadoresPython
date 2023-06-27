from django.http import HttpResponse
from django.template import Template, Context, loader


def lobby(request):
    return HttpResponse("<h1>Bienvenidos a InstaBlog<h1>")


def perfil(request):
    return HttpResponse("<h1>Hola petones<h1>")


def inicioInvocador(self):
    miHtml = open(
        "C:/Users/Usuario/Desktop/Instablog/InstaBlog/InstaBlog/plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContext = Context()
    documento = plantilla.render(miContext)
    return HttpResponse(documento)


# plantilla = loader.get_template("template1.html")
# documento = plantilla.render(diccionario)
# return HttpResponse(documento)
