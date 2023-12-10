from django.shortcuts import render

from .models import Project #desde models importamos la clase Project

# Create your views here.

def portfolio(request) :
    projects = Project.objects.all() # creamos una lista, que hace referencia a una lista de los objetos de la clase Project
    return render(request,"portfolio/portfolio.html", {'projects':projects}) #inyectamos la lista de proyectos en el template y para pasar datos y le pasamos un tercer parámetro con un diccionario (de contexto) y le pasamos la variable