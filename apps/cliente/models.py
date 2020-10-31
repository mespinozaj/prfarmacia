from django.db import models
from apps.persona.models import Persona


# Se importa modelo Persona para los demás atributos
# Creacion del modelo Cliente, 


class Cliente(Persona):
	nit = models.CharField('NIT', null=False, blank=False, 
		max_length=10)


	def __str__(self):
		return (self.nombre + ' ' + self.apellido)


	class Meta():
		db_table = 'cliente'
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'





