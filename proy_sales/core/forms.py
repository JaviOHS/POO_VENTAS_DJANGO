from django import forms
from core.models import Product
from core.models import Brand
from core.models import Supplier
from core.models import Category
from django.utils import timezone
import datetime

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    dni = forms.CharField(max_length=10, label='DNI')
    first_name = forms.CharField(max_length=30, label='Nombres')
    last_name = forms.CharField(max_length=150, label='Apellidos')
    celular = forms.CharField(max_length=15, required=False, label='Celular')
    correo = forms.EmailField(required=False, label='Correo electrónico')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'dni', 'first_name', 'last_name', 'celular', 'correo', 'password1', 'password2')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'price', 'stock', 'brand', 'categories', 'line', 'supplier', 'expiration_date', 'image', 'state']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese descripción del producto', 'id': 'id_description'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese precio del producto', 'id': 'id_price'}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese stock del producto', 'id': 'id_stock'}),
            'brand': forms.Select(attrs={'class': 'form-select', 'id': 'id_brand'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-select', 'id': 'id_categories'}),
            'line': forms.Select(attrs={'class': 'form-select', 'id': 'id_line'}),
            'supplier': forms.Select(attrs={'class': 'form-select', 'id': 'id_supplier'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'id_expiration_date'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'id_image'}),
            'state': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'id_state'}),
        }
        labels = {
            'description': 'Producto',
            'price': 'Precio',
            'stock': 'Stock',
            'brand': 'Marca',
            'categories': 'Categoría',
            'line': 'Línea',
            'supplier': 'Proveedor',
            'expiration_date': 'Fecha de vencimiento',
            'image': 'Imagen',
            'state': 'Estado',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Solo establecer el valor predeterminado si el objeto es nuevo
            self.fields['expiration_date'].initial = (timezone.now() + datetime.timedelta(days=30)).date().isoformat()

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['description', 'state']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese descripción de la marca'}),
            'state': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'description': 'Nombre de la marca',
            'state': 'Estado', # Agrega la etiqueta para el campo 'state'
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','ruc','address','phone', 'state', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del proveedor', 'id': 'id_name'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese RUC del proveedor', 'id': 'id_ruc'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese dirección del proveedor'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese número celular', 'id': 'id_phone'}),
            'state': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'id': 'id_image'}),
        }
        labels = {
            'name': 'Nombre',
            'ruc': 'RUC',
            'address': 'Dirección',
            'phone': 'Celular',
            'state': 'Estado',
            'image': 'Imagen',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['description','state']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese categoría'}),
            'state': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'description': 'Categoría',
            'state': 'Estado', 
        }
