import datetime
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Brand(models.Model):
    description = models.CharField('Articulo',max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Estado', default = True)
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['description']
        indexes = [models.Index(fields=['description']),]
    def __str__(self):
        return self.description

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    ruc = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Estado', default = True)
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
    def __str__(self):
        return self.name
    

class Product(models.Model):
    class Status(models.TextChoices):
        STORE = 'RS', 'Rio Store'
        FERRISARITO = 'FS', 'Ferrisariato'
        COMISARIATO = 'CS', 'Comisariato'
    description = models.CharField('Articulo',max_length=100)
    price=models.DecimalField('Precio',max_digits=10,decimal_places=2,default=Decimal('0.0'))
    stock=models.IntegerField('Stock',default=100)
    expiration_date = models.DateTimeField('Fecha Caducidad',default=timezone.now()+datetime.timedelta(days=30))
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='product',verbose_name='Marca')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    supplier = models.OneToOneField(Supplier,on_delete=models.CASCADE,verbose_name='Proveedor')
    categories = models.ManyToManyField('Category',verbose_name='Categoria')
    line = models.CharField('Linea',max_length=2,choices=Status.choices,default=Status.COMISARIATO)
    image = models.ImageField(upload_to='products/',blank=True,null=True,default='products/default.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Estado', default = True)
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

class Category(models.Model):
    description = models.CharField(verbose_name='Categoria',max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Estado', default = True)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['description']
        indexes = [models.Index(fields=['description']),]
    def __str__(self):
        return self.description
