from django.shortcuts import render
# voy a trabajar con vistas genericas
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
    )

from .models import Prueba

class PruebaView(TemplateView):
    #Esto es un standar, siempre se debe hacer
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    #model = MODEL_NAME
    #Esto no porque todavia no voy a user bases de datos, voy a usar en su ligar queryset
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'
   

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    fields = ['titulo', 'subtitulo', 'cantidad']
