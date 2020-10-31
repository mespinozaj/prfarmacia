from django.contrib import admin
from . models import *
# Register your models here.


class DetalleCompraInLine(admin.TabularInline):
	
	model = DetalleCompra
	extra = 1

	fields = [

		'comprobantecompra',
		'producto', 
		'numeroloteproducto',
		'cantidad',
		'fechavencimiento',
		'ubicacion',
		'preciocompra', 
		'precioventa',
		'subtotal'
	]

	readonly_fields = ['subtotal']
	# campo de solo mostrar

	autocomplete_fields = ['producto']
	#autocompletar 

class ComprobanteCompraAdmin(admin.ModelAdmin):

	inlines = [DetalleCompraInLine]
	readonly_fields = ['total']
	# campo de solo mostrar
	
	list_filter = ['fecha']	
	list_display = ['proveedor', 'fecha','total','compc']
	list_per_page = 15
	# solo mostrar 15 por pagina
	
	date_hierarchy = "fecha"

	ordering = ['-fecha']
	autocomplete_fields = ['proveedor']
	#autocompletar




admin.site.register(ComprobanteCompra, ComprobanteCompraAdmin)