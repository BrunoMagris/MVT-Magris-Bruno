from django.shortcuts import render
from AppFamilia.models import *
from django.http import HttpResponse
from AppFamilia.Templates import*
from django.template import Template, Context, loader

#Create your views here.

def Familia(request):#Agregar Familiares

    familiar = Familiares(nombre="Ismael", apellido = "Magris", edad =9, proximo_cumpleaños = "2023-08-15")     
    
    familiar.save()

    return HttpResponse(f"Estoy guardando a mis familiares {familiar.nombre}")



def ver_Familiares(request):
    queryset = Familiares.objects.all()
    diccionario = {"Familiares":queryset}
    plantilla = loader.get_template("AppFamilia/Familiares.html")
    documento_html = plantilla.render(diccionario)
    return HttpResponse(documento_html)