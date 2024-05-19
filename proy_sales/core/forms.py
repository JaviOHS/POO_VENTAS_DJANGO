from django import forms
from core.models import Product
from core.models import Brand
from core.models import Supplier
from core.models import Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description','price','stock','brand','categories','line','supplier','expiration_date','image','state']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['description','state']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','ruc','address','phone', 'state']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['description','state']
