from django.contrib import admin
from django.shortcuts import redirect
from .models import *
# Register your models here.


class DetalleVentaInLine(admin.TabularInline):
	
	model = DetalleVenta
	extra = 1

	fields = [

		'comprobanteventa',
		'producto',
		'numerolote', 
		'cantidad',
		'subtotal',

	]

	readonly_fields = ['subtotal']
	# campo de solo para mostrar

	autocomplete_fields = ['producto']
	#comando para autocompletar


class ComprobanteVentaAdmin(admin.ModelAdmin):

	inlines = [DetalleVentaInLine]
	readonly_fields = ['total', 'vuelto']
	#campo de solo para mostrar
	
	list_filter = ['fecha']
	list_display = ['cliente', 'fecha', 'comp']
	list_per_page = 15
	#listados por pagina
	ordering = ['-fecha']
	date_hierarchy = "fecha"


	# se manda a llamar al template
	def impr_prods(self, request, queryset):
		return redirect('/InformeTodasVentas')
	impr_prods.short_description = 'Ventas'

	def impr_prods(self, request, queryset):
		return redirect('/InformeVentasDia')
	impr_prods.short_description = 'VentasDia'

	
admin.site.register(ComprobanteVenta, ComprobanteVentaAdmin)	