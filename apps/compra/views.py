from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from .models import *
from django.shortcuts import redirect

# Create your views here.


class ComprobanteCompraview(PDFTemplateView):
    # se crea la clase para crear el comprobante de compras
    template_name = "ComprobanteCompra.html"

    def get_context_data(self, **kwargs):
        # se crea el metodo de get_context
        ids = self.request.GET.get("id")
        comprobantec = ComprobanteCompra.objects.get(id=ids)
        # se crea la variable comprobantec el cual recupera todos los comprobantes
        detalle3 = DetalleCompra.objects.filter(comprobantecompra=comprobantec.id)
        # se crea la variable detalle3 para obtener todos los detalles de compras
        return super(ComprobanteCompraview, self).get_context_data(
            pagesize="Letter",
            title="Comprobante de Compras",
            # se manda al comprobante de compras las variables comprobantec y detalle3
            comprobantec=comprobantec,
            detalle3=detalle3,
            **kwargs
            )