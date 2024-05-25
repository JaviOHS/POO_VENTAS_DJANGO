import datetime
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import Group


class Brand(models.Model):
    description = models.CharField('Articulo', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['description']
        indexes = [models.Index(fields=['description'])]

    def __str__(self):
        return self.description

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    ruc = models.CharField(max_length=13)  # RUC tiene 13 dígitos en Ecuador
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Estado', default=True)
    image = models.ImageField(upload_to='suppliers/', blank=True, null=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name

class Category(models.Model):
    description = models.CharField('Categoría', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['description']
        indexes = [models.Index(fields=['description'])]

    def __str__(self):
        return self.description

def get_default_expiration_date():
    return timezone.now() + datetime.timedelta(days=30)

class Product(models.Model):
    class Status(models.TextChoices):
        STORE = 'RS', 'Rio Store'
        FERRISARITO = 'FS', 'Ferrisariato'
        COMISARIATO = 'CS', 'Comisariato'

    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=100)
    expiration_date = models.DateTimeField(default=timezone.now() + datetime.timedelta(days=30))
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product', verbose_name='Marca')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE, verbose_name='Proveedor')
    categories = models.ManyToManyField('Category', verbose_name='Categoria')
    line = models.CharField(max_length=2, choices=Status.choices)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['description']
        indexes = [models.Index(fields=['description']),]

    def __str__(self):
        return self.description

    @property
    def get_categories(self):
        return " - ".join([c.description for c in self.categories.all().order_by('description')])
    
