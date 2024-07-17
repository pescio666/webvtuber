from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now())
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    estado = models.CharField(max_length=20, default="EN PREPARACION")

    def __str__(self):
        return str(self.id)+" "+self.cliente.username+" "+str(self.fecha)[0:16]

class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    detalle = models.CharField(max_length=200)
    descripcion_producto = models.CharField(max_length=500, default="Sin informacion")
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')  #Recordar instalar libreria pillow 'pip install Pillow' para subir y ver imagenes locales en la db django.

    def __str__(self):
        return self.detalle+" ("+self.codigo+")"
        
class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()


    def __str__(self):
        return str(self.id)+" "+self.producto.detalle[0:20]+" "+str(self.venta.id)
    
class Talento(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    gustos = models.CharField(max_length=20, default='', blank=True)
    edad = models.IntegerField(default=None, blank=True, null=True)
    altura = models.FloatField(default=None, blank=True, null=True)
    imagen = models.ImageField(upload_to='talentos/', default='talentos/default_image.jpg')
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre+" ("+self.tipo+")"
