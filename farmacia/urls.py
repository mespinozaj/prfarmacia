"""farmacia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.venta.views import ComprobanteVentaview
from apps.producto.views import Productoview
from apps.compra.views import ComprobanteCompraview
from apps.producto.views import FichadeProductos
from apps.venta.views import FichadeVentas
from apps.venta.views import FichadeVentasDia
from apps.producto.views import FichadeProductosProximosVencer
from apps.producto.views import FichadeProductosProximosVencer2
from apps.producto.views import FichadeProductosProximosVencer3

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^comprobante/(?P<id>)",ComprobanteVentaview.as_view()),
 
   	url(r"^informe/(?P<id>)",Productoview.as_view()),

  	url(r"^comprobantec/(?P<id>)",ComprobanteCompraview.as_view()),
	
  	url(r"^InformeTodosProductos/", FichadeProductos.as_view(
        ), name="informeproductos"),
  	url(r"^InformeTodasVentas/", FichadeVentas.as_view(
        ), name="informeventas"),
    url(r"^InformeVentasDia/", FichadeVentasDia.as_view(
        ), name="infventasdia"),
    url(r"^InformeProductosProximosVencer/", FichadeProductosProximosVencer.as_view(
        ), name="informeproductospv"),
    url(r"^InformeProductosProximosVencer2/", FichadeProductosProximosVencer2.as_view(
        ), name="informeproductospv2"),
    url(r"^InformeProductosProximosVencer3/", FichadeProductosProximosVencer3.as_view(
        ), name="informeproductospv3"),
	]

