from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

#registra el proyecto en el sitio, a través del administrador
admin.site.register(Project,ProjectAdmin)