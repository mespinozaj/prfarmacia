from django.contrib import admin
from .models import *

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	
	search_fiels= ['nombre']
	list_filter = ['nombre']
	list_display = ['nombre', 'apellido', 'direccion', 'telefono', 'nit']

	list_per_page = 15

	

admin.site.register(Cliente, ClienteAdmin)

