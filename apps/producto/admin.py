from django.contrib import admin
from django.shortcuts import redirect
from .models import *

# Register your models here.
class DetalleProductoInLine(admin.TabularInline):
	
	model = DetalleProducto
	extra = 1

	fields = [

		'producto',
		'numeroloteproducto', 
		'cantidad',
		'preciocompra',
		'precioventa',
		'fechavencimiento',
		'fechacompra',
		'ubicacion',
	]

	readonly_fields = ['producto', 
						'numeroloteproducto', 
						'cantidad',
						'preciocompra',
						'precioventa',
						'fechavencimiento',
						'fechacompra',
						'ubicacion',
						]



class ProductoAdmin(admin.ModelAdmin):

	search_fields = ['nombre']
	inlines = [DetalleProductoInLine]
	list_per_page = 15
	autocomplete_fields = ['laboratorio', 'tipopresentacion']
	readonly_fields = ['existencia']
	list_display = ['nombre', 'laboratorio', 'tipopresentacion', 'existencia', 'inf']
	#autocompletar

	# se manda a llamar al template
	def impr_prods(self, request, queryset):
		return redirect('/InformeTodosProductos')
	impr_prods.short_description = 'Productos'

	def impr_prods(self, request, queryset):
		return redirect('/InformeProductosProximosVencer')
	impr_prods.short_description = 'ProductosProximosVencer'

	def impr_prods(self, request, queryset):
		return redirect('/InformeProductosProximosVencer2')
	impr_prods.short_description = 'ProductosProximosVencer2'

	def impr_prods(self, request, queryset):
		return redirect('/InformeProductosProximosVencer3')
	impr_prods.short_description = 'ProductosProximosVencer3'

class UbicacionAdmin(admin.ModelAdmin):

	search_fields = ['nombre']
	# inlines = [DetalleProductoInLine]
	list_per_page = 15

class LaboratorioAdmin(admin.ModelAdmin):

	search_fields = ['nombre']
	# inlines = [DetalleProductoInLine]
	list_per_page = 15

class TipoPresentacionAdmin(admin.ModelAdmin):

	search_fields = ['nombre']
	# inlines = [DetalleProductoInLine]
	list_per_page = 15


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(TipoPresentacion, TipoPresentacionAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)

# Register your models here.

