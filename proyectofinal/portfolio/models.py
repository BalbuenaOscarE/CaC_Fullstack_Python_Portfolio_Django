from django.db import models

#acá vamos a empezar a enlazar cosas con lo que va a ser nuestra base de datos ( se usa para eso)

# Create your models here.

class Project(models.Model):
    #esto va a representar la tabla que va a estar en la base de datos
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    #éstas 2 sirven para crear y modificar desde django lo que nosotros queramos
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación") #que nos diga cuando fue creado
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha modificación") #que nos diga cuando fue actualizado

    def __str__(self):
        return self.title

class Meta:
    verbose_name = "proyecto"
    verbose_name_plural = "proyectos"
    ordering = ["-created"] #orden del más nuevo al más antiguo, si saco el guión lo muestra al revés