from django.db import models
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado
from apps.producto.models import Producto, DetalleProducto
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.db import transaction
from datetime import date

# se crea el modelo ComprobanteVenta

class ComprobanteVenta(models.Model):
	fecha = models.DateField('Fecha', default=date.today,
		null=False, blank=False)
	cliente = models.ForeignKey(
		Cliente, on_delete=models.CASCADE, null=False, blank=False)
	empleado = models.ForeignKey(
		Empleado, on_delete=models.CASCADE, null=False, blank=False)
	total = models.FloatField(
		'total', null=True, blank=True, default=0.00)
	efectivo = models.FloatField(
		'efectivo', null=True, blank=True, default=0)
	vuelto = models.FloatField(
		'vuelto', null=True, blank=True, default=0)

	
	def comp(self): 
		return mark_safe(
			u'<center><a href="/comprobante/?id=%s" target="_blank">Comprobante</a></center>' % self.id)


	def save (self, force_insert=False, force_update=False, using=None):

		self.vuelto = (self.efectivo - self.total)

		super(ComprobanteVenta, self).save(force_insert, force_update, using)


	class Meta():
		db_table = 'comprobanteventa'
		verbose_name = 'Comprobante Venta'
		verbose_name_plural = 'Comprobante de Venta'


# se crea el modelo DetalleVenta

class DetalleVenta(models.Model):
	
	comprobanteventa = models.ForeignKey(
		ComprobanteVenta, on_delete=models.CASCADE, 
		null=True, blank=True,
		related_name='Detalle')
	producto = models.ForeignKey(
		Producto, on_delete=models.CASCADE, null=False, blank=False)
	numerolote = models.CharField('Numero de lote', null=False, blank=False, 
		max_length=50)
	cantidad = models.PositiveIntegerField('Cantidad',
		null=False, blank=False)
	subtotal = models.FloatField(
		'subtotal', null=True, blank=True, default=0.00)


	# se crea metodo para verificar los valores unicamente al ingresarlos	
	def clean(self):
		if not self.pk:
			isnew = True
		else:
			isnew = False
		with transaction.atomic():
			if isnew:
		
				# metodo para verificar si existe el numerodelote de un producto
				mp = DetalleProducto.objects.filter(producto = self.producto).filter(numeroloteproducto = self.numerolote).first()
				
				if mp: 	
					
					# metodo para verificar las existencias
					pro = Producto.objects.filter(nombre = self.producto.nombre).first()
					print(pro)


					if pro.existencia < self.cantidad: 	
						
						raise ValidationError('No hay existencias')
						
						()	
					else: 

						if mp.cantidad < self.cantidad:

							raise ValidationError('No hay la existencia suficiente en este detalle')

						else:
							# metodo para verificar si el producto esta vencido
							if mp.fechavencimiento == None:
								
								()

							else:
							
								if mp.fechavencimiento <= date.today():

									raise ValidationError('El producto ya esta vencido')

								else:

									print(pro.existencia)


				else: 
					raise ValidationError('El numero de lote no existe')


			
		
	def save (self, force_insert=False, force_update=False, using=None):

		mp = DetalleProducto.objects.filter(producto = self.producto).filter(numeroloteproducto = self.numerolote).first()
		
		if mp.fechavencimiento == None:
			# metodo para calcular el subtotal de un producto
			product = DetalleProducto.objects.filter(producto = self.producto).filter(numeroloteproducto = self.numerolote).first()
			print(product)
			print(product.producto)
			print(product.precioventa)
			self.subtotal = (self.cantidad * product.precioventa)

			# metodo para restar existencias de un producto
			rest = Producto.objects.filter(nombre = self.producto).first()
			rest.existencia = (rest.existencia - self.cantidad)
			print(rest.existencia)
			product.cantidad = (product.cantidad - self.cantidad)
			rest.save()
			product.save()
		
			# metodo para sumar el total
			comproventa = ComprobanteVenta.objects.filter(id=self.comprobanteventa.id).first()
			print(comproventa.fecha)
			comproventa.total = (comproventa.total + self.subtotal)
			comproventa.save()
			super(DetalleVenta, self).save(force_insert, force_update, using)

		else:

			if mp.fechavencimiento <= date.today():
				()

			else:
				product = DetalleProducto.objects.filter(producto = self.producto).filter(numeroloteproducto = self.numerolote).first()
				print(product)
				print(product.producto)
				print(product.precioventa)
				self.subtotal = (self.cantidad * product.precioventa)

				# metodo para restar existencias de un producto
				rest = Producto.objects.filter(nombre = self.producto).first()
				rest.existencia = (rest.existencia - self.cantidad)
				print(rest.existencia)
				product.cantidad = (product.cantidad - self.cantidad)
				rest.save()
				product.save()
			
				# metodo para sumar el total
				comproventa = ComprobanteVenta.objects.filter(id=self.comprobanteventa.id).first()
				print(comproventa.fecha)
				comproventa.total = (comproventa.total + self.subtotal)
				comproventa.save()
				
				super(DetalleVenta, self).save(force_insert, force_update, using)

	
	# se define variable pr para obtener el precio en el comprobante de venta			
	def pr (self):
		precio=self.subtotal/self.cantidad
		return precio



	class Meta():
		db_table = 'detalleventa'
		verbose_name = 'Detalle venta'
		verbose_name_plural = 'Detalle de ventas'

