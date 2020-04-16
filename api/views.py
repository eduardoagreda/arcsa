from django.shortcuts import render

# Create your views here.

from api.models import Clientes, ConsumoClientes, PagoCliente, Productos

from api.serializers import ClienteSerializer, ConsumoClientesSerializer, PagoClienteSerializer, ProductosSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ClienteList(APIView):
    serializer_class = ClienteSerializer
    def get(self, request, format=None):
        clientes = Clientes.objects.all()
        if clientes:
            serializer = ClienteSerializer(clientes, many=True)
            result = {'result': serializer.data}
            return Response(result, status=status.HTTP_200_OK)
        result = {'result': 'Error, no se encuentran datos en la base de datos.'}
        return Response(result, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = ClienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class ConsumoClienteList(APIView):
    serializer_class = ConsumoClientesSerializer
    def get(self, request, format=None):
        cClientes = ConsumoClientes.objects.all()
        if cClientes:
            serializer = ConsumoClientesSerializer(cClientes, many=True)
            result = {'result': serializer.data}
            return Response(result, status=status.HTTP_200_OK)
        result = {'result': 'Error, no se encuentran datos en la base de datos.'}
        return Response(result, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = ConsumoClientesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class PagoCLienteList(APIView):
    serializer_class = PagoClienteSerializer
    def get(self, request, format=None):
        pClientes = PagoCliente.objects.all()
        if pClientes:
            serializer = PagoClienteSerializer(pClientes, many=True)
            result = {'result': serializer.data}
            return Response(result, status=status.HTTP_200_OK)
        result = {'result': 'Error, no se encuentran datos en la base de datos.'}
        return Response(result, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = PagoClienteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ProductoList(APIView):
    serializer_class = ProductosSerializer
    def get(self, request, format=None):
        producto = Productos.objects.all()
        if producto:
            serializer = ProductosSerializer(producto, many=True)
            result = {'result': serializer.data}
            return Response(result, status=status.HTTP_200_OK)
        result = {'result': 'Error, no se encuentran datos en la base de datos.'}
        return Response(result, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = ProductosSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)