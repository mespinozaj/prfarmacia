from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from .models import *
from django.shortcuts import redirect
from datetime import datetime, date



class Productoview(PDFTemplateView):
    # se crea la clase para crear el informe de productos
    template_name = "InformeProductos.html"

    def get_context_data(self, **kwargs):
        # se crea el metodo de get_context
        ids = self.request.GET.get("id")
        informe = Producto.objects.get(id=ids)
        # se crea la variable informe el cual recupera todos los productos
        detalle2 = DetalleProducto.objects.filter(producto=informe.id)
        # se crea la variable detalle2 para obtener todos los detalles de productos
        return super(Productoview, self).get_context_data(
            pagesize="Letter",
            title="Informe de Productos",
            # se manda al informe de productos las variables informe y detalle2
            informe=informe,
            detalle2=detalle2,
            **kwargs
            )

class FichadeProductos(PDFTemplateView):
    # se crea la clase de Ficha de Productos para poder generar informe de Productos
    template_name = "InformeTodosProductos.html"

    def get_context_data(self, **kwargs):
        # la variable detalle2 recoge todos los detalles de productos existentes
        detalle2 = DetalleProducto.objects.exclude(cantidad=0)
        day = date.today()
        # la variable day captura la fecha de hoy
        return super(FichadeProductos, self).get_context_data(
            pagesize="Letter",
            title="Productos",
            detalle2=detalle2,
            # detalle2 manda la variable detalle2 que es donde están todos los detalles de productos al template
            day=day,
            # se manda la variable day con la fecha de hoy al template
            **kwargs
            )

class FichadeProductosProximosVencer(PDFTemplateView):
    # se crea la clase de Ficha de Productos Proximos Vencer para poder generar informe de Productos 
    # proximos a vencer al año
    template_name = "InformeProductosProximosVencer.html"

    def get_context_data(self, **kwargs):
        # la variable detalle2 recoge todos los detalles de productos existentes
        detalle2 = DetalleProducto.objects.exclude(cantidad=0)
        day = datetime.now().date()
        year = datetime.year
        # la variable day captura la fecha de hoy
        return super(FichadeProductosProximosVencer, self).get_context_data(
            pagesize="Letter",
            title="ProductosProximosVencer",
            detalle2=detalle2,
            # detalle2 manda la variable detalle2 que es donde están todos los detalles de productos al template
            day=day,
            year=year,
            # se manda la variable day con la fecha de hoy al template
            **kwargs
            )

class FichadeProductosProximosVencer2(PDFTemplateView):
    # se crea la clase de Ficha de Productos Proximos Vencer 2 para poder generar informe de Productos
    # prixmos a vencer dentro de un mes
    template_name = "InformeProductosProximosVencer2.html"

    def get_context_data(self, **kwargs):
        # la variable detalle2 recoge todos los detalles de productos existentes
        detalle2 = DetalleProducto.objects.exclude(cantidad=0)
        day = datetime.now().date()
        month = datetime.month
        # la variable day captura la fecha de hoy
        return super(FichadeProductosProximosVencer2, self).get_context_data(
            pagesize="Letter",
            title="ProductosProximosVencer2",
            detalle2=detalle2,
            # detalle2 manda la variable detalle2 que es donde están todos los detalles de productos al template
            day=day,
            month=month,
            # se manda la variable day con la fecha de hoy al template
            **kwargs
            )

class FichadeProductosProximosVencer3(PDFTemplateView):
    # se crea la clase de Ficha de Productos Proximos a Vencer 3 para poder generar informe de Productos
    # Vencidos
    template_name = "InformeProductosProximosVencer3.html"

    def get_context_data(self, **kwargs):
        # la variable detalle2 recoge todos los detalles de productos existentes
        detalle2 = DetalleProducto.objects.exclude(cantidad=0)
        day = datetime.now().date()
        # la variable day captura la fecha de hoy
        return super(FichadeProductosProximosVencer3, self).get_context_data(
            pagesize="Letter",
            title="ProductosProximosVencer3",
            detalle2=detalle2,
            # detalle2 manda la variable detalle2 que es donde están todos los detalles de productos al template
            day=day,
            # se manda la variable day con la fecha de hoy al template
            **kwargs
            )