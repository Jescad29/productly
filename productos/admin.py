from django.contrib import admin
from .models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('nombre', 'stock', 'creado_en')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)

