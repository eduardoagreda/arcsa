from django.contrib import admin

# Register your models here.
from api.models import Clientes, ConsumoClientes, PagoCliente, Productos

admin.site.register(Clientes)
admin.site.register(ConsumoClientes)
admin.site.register(PagoCliente)
admin.site.register(Productos)