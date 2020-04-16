from django.urls import path

from api.views import ClienteList, ConsumoClienteList, PagoCLienteList, ProductoList

urlpatterns = [
    path('cliente', ClienteList.as_view()),
    path('consumo', ConsumoClienteList.as_view()),
    path('pago', PagoCLienteList.as_view()),
    path('producto', ProductoList.as_view()),
]