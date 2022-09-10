from django.shortcuts import render
from AppFamilia.models import Familiares
from django.http import HttpResponse
# Create your views here.

def Familia(request):

    familiar = Familiares(nombre="Ismael", apellido = "Magris", edad =9, proximo_cumpleaños = "2023-08-15")

    familiar.save()

    return HttpResponse(f"Estoy guardando a mis familiares {familiar.nombre}")
