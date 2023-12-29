from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje =models.FloatField()
    # CASCADE: eliminar el producto
    # PROTECT: lanza error si se quiere eliminar la categoria
    #RESTRICT: Solo elimina la categoria si no existen productos.
    #SET_NULL: Actualiza a valor nulo en el caso de que se elimine la categoria
    # SET_DEFAULT: Asigna un valor por defecto.
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE
    )
    #ahora que ya tenemos nuestros modelos lo que sigue es actualizar nuestra base de datos ya que queremos que estos modelos se vean reflejados en nuestra base de datos
    creado_en = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre
    