from django.contrib import admin

# Register your models here.

# Registrando mis Modelos
from . models import Alumno

# Registrando el Modelo
admin.site.register(Alumno)