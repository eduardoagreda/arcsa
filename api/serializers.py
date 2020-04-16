from rest_framework import serializers
from api.models import Clientes, Productos, ConsumoClientes, PagoCliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ('__all__')

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('__all__')

class ConsumoClientesSerializer(serializers.ModelSerializer):
    productos = ProductosSerializer(read_only=True)
    cliente = ClienteSerializer(read_only=True)
    class Meta:
        model = ConsumoClientes
        fields = ('__all__')

class PagoClienteSerializer(serializers.ModelSerializer):
    consumo = ConsumoClientesSerializer(read_only=True)
    class Meta:
        model = PagoCliente
        fields = ('__all__')