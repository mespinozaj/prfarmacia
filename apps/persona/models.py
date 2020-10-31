from django.db import models
from django.db import models

# Creacion del modelo persona

class Persona(models.Model):
	nombre = models.CharField('nombres', null=False, blank=False, max_length=50)
	apellido = models.CharField('apellidos', null=False, blank=False, max_length=50)
	direccion = models.CharField('direccion', null=False, blank=False, max_length=100, default='')
	telefono = models.CharField('telefono', null=False, blank=False, max_length=8, default=0)

