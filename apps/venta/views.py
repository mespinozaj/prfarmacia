from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from .models import *
from django.shortcuts import redirect
from datetime import date




class ComprobanteVentaview(PDFTemplateView):
    # se crea la clase para crear el comprobante de ventas
    template_name = "InformeVenta.html"

    def get_context_data(self, **kwargs):
        # se crea el metodo de get_context
        ids = self.request.GET.get("id")
        comprobante = ComprobanteVenta.objects.get(id=ids)
        # se crea la variable comprobante el cual recupera todos los comprobantes
        detalle = DetalleVenta.objects.filter(comprobanteventa=comprobante.id)
        # se crea la variable detalle para obtener todos los detalles de ventas
        return super(ComprobanteVentaview, self).get_context_data(
            pagesize="Letter",
            title="Comprobante de Ventas",
            # se manda al comprobante de ventas las variables comprobante y detalle
            comprobante=comprobante,
            detalle=detalle,
            **kwargs
            )

class FichadeVentas(PDFTemplateView):
    # se crea la clase de Ficha de Ventas para poder generar informe de Ventas 
    template_name = "InformeTodasVentas.html"

    def get_context_data(self, **kwargs):
        # la variable detalle recoge todos los detalles existentes
        detalle = DetalleVenta.objects.all()
        day = date.today()
        # la variable day captura la fecha de hoy
        t=0
        for hola in detalle: 

            t = (t+hola.subtotal)
        return super(FichadeVentas, self).get_context_data(
            pagesize="Letter",
            t=t,
            title="Ventas",
            detalle=detalle,
            # detalle manda la variable detalle es donde estan todos los detalles de productos al template
            day=day,
            # se manda la variable day con la fecha de hoy al template
            **kwargs
            )

class FichadeVentasDia(PDFTemplateView):
    # se crea la clase de Ficha de Ventas Dia para poder generar informe de Ventas que se realizaron durante el dia 
    template_name = "InformeVentasDia.html"

    def get_context_data(self, **kwargs):
        day = date.today()
        # la variable detalle recoge todos los detalles existentes
        detalle = ComprobanteVenta.objects.filter(fecha=day)
        # la variable day captura la fecha de hoy
        t=0
        for hola in detalle: 

            t = (t+hola.total)
        return super(FichadeVentasDia, self).get_context_data(
            pagesize="Letter",
            t=t,
            title="VentasDia",
            detalle=detalle,
            # detalle manda la variable detalle es donde estan todos los detalles de productos al template
            day=day,
            # se manda la variable day con la fecha de hoy al template
            **kwargs
            )