from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from core.forms import ProductForm, BrandForm, SupplierForm, CategoryForm
from core.models import Product, Brand, Supplier, Category
from django.conf import settings
import os

# ----------------- Vistas de Home -----------------
def home(request):
   data = {"title1":"Autor | TeacherCode", "title2":"Super Mercado Economico"}
   return render(request,'core/home.html',data)

# ----------------- Vistas de Productos -----------------
def product_List(request):
    data = {"title1": "Productos","title2": "Consulta De Productos"}
    products = Product.objects.all() # select * from Product
    data["products"]=products
    return render(request,"core/products/list.html",data)

# Crear un producto
def product_create(request):
    data = {"title1": "Productos","title2": "Ingreso De Productos"}
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("core:product_list")
    else:
        data["form"] = ProductForm() # controles formulario sin datos
    return render(request, "core/products/form.html", data)

# Editar un producto
def product_update(request,id):
    data = {"title1": "Productos","title2": "Edicion De Productos"}
    product = Product.objects.get(pk=id)
    if request.method == "POST":
      form = ProductForm(request.POST,request.FILES, instance=product)
      if form.is_valid():
            form.save()
            return redirect("core:product_list")
    else:
        form = ProductForm(instance=product)
        data["form"]=form
    return render(request, "core/products/form.html", data)

# Eliminar un producto
def product_delete(request,id):
    product = Product.objects.get(pk=id)
    data = {"title1":"Eliminar","title2":"Eliminar Un Producto","product":product}
    if request.method == "POST":
        product.delete()
        return redirect("core:product_list")
    return render(request, "core/products/delete.html", data)

# ----------------- Vistas de Marcas -----------------
def brand_List(request):
    data = {"title1": "Marcas", "title2": "Consulta De Marcas De Productos"}
    brands = Brand.objects.all() # select * from Product
    data["brands"]=brands
    return render(request,"core/brands/list.html",data)

# Crear una marca
def brand_create(request):
    data = {"title1": "Marcas","title2": "Ingreso De Marcas"}
    if request.method == "POST":
        #print(request.POST)
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = request.user
            brand.save()
            return redirect("core:brand_list")
    else:
        data["form"] = BrandForm() # controles formulario sin datos
    return render(request, "core/brands/form.html", data)

# Editar una marca
def brand_update(request,id):
    data = {"title1": "Marcas", "title2": "Edicion De Marcas"}
    brand = Brand.objects.get(pk=id)
    if request.method == "POST":
      form = BrandForm(request.POST,request.FILES, instance=brand)
      if form.is_valid():
            form.save()
            return redirect("core:brand_list")
    else:
        form = BrandForm(instance=brand)
        data["form"]=form
    return render(request, "core/brands/form.html", data)

# Eliminar una marca
def brand_delete(request,id):
    brand = Brand.objects.get(pk=id)
    data = {"title1":"Eliminar","title2":"Eliminar Una Marca","brand":brand}
    if request.method == "POST":
        brand.delete()
        return redirect("core:brand_list")
    return render(request, "core/brands/delete.html", data)

# ----------------- Vistas de Proveedores -----------------
def supplier_List(request):
    data = {"title1": "Proveedores", "title2": "Consulta De Proovedores De Productos"}
    suppliers = Supplier.objects.all() # select * from Product
    data["suppliers"]=suppliers
    return render(request,"core/suppliers/list.html",data)

# Crear un proveedor
def supplier_create(request):
    data = {"title1": "Proveedores","title2": "Ingreso De Proveedores"}
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.user = request.user
            supplier.save()
            return redirect("core:supplier_list")
    else:
        data["form"] = SupplierForm()
    return render(request, "core/suppliers/form.html", data)

# Editar un proovedor
def supplier_update(request,id):
    data = {"title1": "Proveedores", "title2": "Edicion De Proveedores"}
    supplier = Supplier.objects.get(pk=id)
    if request.method == "POST":
      form = SupplierForm(request.POST,request.FILES, instance=supplier)
      if form.is_valid():
            form.save()
            return redirect("core:supplier_list")
    else:
        form = SupplierForm(instance=supplier)
        data["form"]=form
    return render(request, "core/suppliers/form.html", data)

# Eliminar una marca
def supplier_delete(request,id):
    supplier = Supplier.objects.get(pk=id)
    data = {"title1":"Eliminar","title2":"Eliminar al Proveedor","supplier":supplier}
    if request.method == "POST":
        supplier.delete()
        return redirect("core:supplier_list")
    return render(request, "core/suppliers/delete.html", data)

# ----------------- Vistas de Categorias -----------------
def category_List(request):
    data = {"title1": "Categorias", "title2": "Consulta De Categorias De Productos"}
    categories = Category.objects.all()
    data["categories"] = categories
    return render(request, "core/categories/list.html", data)

# Crear una categoria
def category_create(request):
    data = {"title1": "Categorias", "title2": "Ingreso De Categorias"}
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect("core:category_list")
    else:
        data["form"] = CategoryForm()
    return render(request, "core/categories/form.html", data)

# Editar una categoria
def category_update(request, id):
    data = {"title1": "Categorias", "title2": "Edicion De Categorias"}
    category = Category.objects.get(pk=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect("core:category_list")
    else:
        form = CategoryForm(instance=category)
        data["form"] = form
    return render(request, "core/categories/form.html", data)

# Eliminar una categoria
def category_delete(request, id):
    category = Category.objects.get(pk=id)
    data = {"title1": "Eliminar", "title2": "Eliminar Una Categoria", "category": category}
    if request.method == "POST":
        category.delete()
        return redirect("core:category_list")
    return render(request, "core/categories/delete.html", data)

