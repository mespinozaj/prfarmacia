from django.contrib import admin
from .models import *

# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
	search_fields= ['nombre', 'apellido']
	list_filter = ['nombre']
	list_display = ['nombre', 'apellido', 'direccion', 'telefono', 'nit']
	list_per_page = 15



admin.site.register(Proveedor, ProveedorAdmin)

# Register your models here.
