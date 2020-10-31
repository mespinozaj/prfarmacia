from django.db import models
from apps.proveedor.models import Proveedor
from apps.producto.models import Producto, DetalleProducto, Ubicacion
from datetime import date
from django.utils.safestring import mark_safe

# Creacion del modelo ComprobanteCompra

class ComprobanteCompra(models.Model):
	
	fecha = models.DateField('Fecha', default=date.today, 
		null=False, blank=False)
	proveedor = models.ForeignKey(
		Proveedor, on_delete=models.CASCADE, null=False, blank=False)
	total = models.FloatField(
		'total', null=False, blank=True, default=0.00)

	def compc(self): 
		return mark_safe(
			u'<center><a href="/comprobantec/?id=%s" target="_blank">Comprobantec</a></center>' % self.id)


	class Meta():
		db_table = 'comprobantecompra'
		verbose_name = 'Comprobante Compra'
		verbose_name_plural = 'Comprobante de Compra'

# Creacion del modelo DetalleCompra

class DetalleCompra(models.Model):

	comprobantecompra = models.ForeignKey(
		ComprobanteCompra, on_delete=models.CASCADE, 
		null=False, blank=False,
		related_name='DetalleCompra')
	producto = models.ForeignKey(
		Producto, on_delete=models.CASCADE, null=False, blank=False)
	numeroloteproducto = models.CharField('Numero de lote del producto',
		null=False, blank=False, max_length=50)
	cantidad = models.PositiveIntegerField('Cantidad', 
		null=False, default=0)
	fechavencimiento = models.DateField('Fecha de vencimiento',
		null=True, blank=True)
	ubicacion = models.ForeignKey(
		Ubicacion, on_delete=models.CASCADE, null=False, blank=False)
	preciocompra = models.FloatField('Precio del costo', 
		null=False, blank=False, default=0)
	precioventa = models.FloatField('Precio venta',
		null=False, blank=False, default=0)
	subtotal = models.FloatField(
		'subtotal', null=True, blank=True, default=0.00)


	class Meta():
		db_table = 'detallecompra'
		verbose_name = 'Detalle compra'
		verbose_name_plural = 'Detalle de compras'


	

	def save (self, force_insert=False, force_update=False, using=None):

		# metodo para la operación del subtotal
		self.subtotal = (self.cantidad * self.preciocompra)

		# metodo para actualizar producto
		jk = DetalleProducto()
		jk.producto = self.producto
		jk.numeroloteproducto = self.numeroloteproducto
		jk.cantidad = self.cantidad
		jk.fechavencimiento = self.fechavencimiento
		jk.ubicacion = self.ubicacion
		jk.preciocompra = self.preciocompra
		jk.precioventa = self.precioventa
		jk.subtotal = self.subtotal
		jk.fechacompra = self.comprobantecompra.fecha
		jk.save()

		# metodo para sumar las existencias del producto
		product = Producto.objects.filter(nombre = self.producto).first()
		product.existencia = (product.existencia + self.cantidad)
		print(product.existencia)
		product.save()

		# metodo para sumar el total de Comprobantecompra
		comprobante = ComprobanteCompra.objects.all().last()
		comprobante.total = (comprobante.total + self.subtotal)
		comprobante.save()

		super(DetalleCompra, self).save(force_insert, force_update, using)



	def delete (self, *args, **kwargs):

		# metodo para restar existencias cuando se le resta la cantidad
		product = Producto.objects.filter(nombre = self.producto).first()
		product.existencia = (product.existencia - self.cantidad)
		print(product.existencia)
		product.save()

		# metodo para restar total cuando se elimina existencias
		comprobante = ComprobanteCompra.objects.all().last()
		comprobante.total = (comprobante.total - self.subtotal)
		comprobante.save()

		comprobante2 = DetalleProducto.objects.filter(producto = self.producto).filter(numeroloteproducto = self.numeroloteproducto).first()
		comprobante2.cantidad = (comprobante2.cantidad - self.cantidad)
		comprobante2.save()


		super(DetalleCompra, self).delete(*args, **kwargs)
