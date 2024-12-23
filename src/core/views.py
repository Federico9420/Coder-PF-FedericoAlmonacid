from django.shortcuts import render
from django.http import HttpResponse


def saludar (request):
    return HttpResponse("Hola desde Django!")

def saludar_con_etiqueta (request):
    return HttpResponse("<h1> Este es el titulo de mi app </h1>")

def saludar_con_parametros (request, nombre, apellido):
    nombre= nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse (f"{apellido}, {nombre}")

def index(request):
    return render(request, "core/index.html")