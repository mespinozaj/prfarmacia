from django.contrib import admin
from .models import *

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
	search_fiels= ['nombre', 'apellido']
	list_filter = ['nombre', 'apellido']
	list_display = ['nombre', 'apellido', 'direccion', 'telefono']

	list_per_page = 15


	

admin.site.register(Empleado, EmpleadoAdmin)

# Register your models here.
