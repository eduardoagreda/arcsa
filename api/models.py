from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellidos = models.CharField(max_length=150, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    curp = models.CharField(max_length=18, blank=True, null=True)
    domicilio = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    

class Productos(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio_unitario = models.IntegerField()

    def __str__(self):
        return self.nombre

class ConsumoClientes(models.Model):
    productos = models.ForeignKey('Productos', related_name='Producto_Consumido', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Clientes', related_name='Consumidor', on_delete=models.CASCADE)

    def __str__(self):
        return self.productos.nombre + ' ' + self.cliente.nombre

class PagoCliente(models.Model):
    consumo = models.ForeignKey("ConsumoClientes", on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total_pagado = models.IntegerField()

    def __str__(self):
        return self.consumo


