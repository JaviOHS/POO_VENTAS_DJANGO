from django.urls import path
from core import views
 
app_name='core' # define un espacio de nombre para la aplicación
urlpatterns = [    
    path('', views.home_guest, name='home'),  # Página de inicio para todos los usuarios
    path('home_guest/', views.home_guest, name='home_guest'),  # Ruta para usuarios no autenticados

    # Otras URLs
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),

    # URLs de vistas
    path('product_list/', views.product_List,name='product_list'),
    path('product_create/', views.product_create,name='product_create'),
    path('product_update/<int:id>/', views.product_update,name='product_update'),
    path('product_delete/<int:id>/', views.product_delete,name='product_delete'),

    # URLs de marcas
    path('brand_list/', views.brand_List,name='brand_list'),
    path('brand_create/', views.brand_create,name='brand_create'),
    path('brand_update/<int:id>/', views.brand_update,name='brand_update'),
    path('brand_delete/<int:id>/', views.brand_delete,name='brand_delete'),

    # URLs de proveedores
    path('supplier_list/', views.supplier_List,name='supplier_list'),
    path('supplier_create/', views.supplier_create,name='supplier_create'),
    path('supplier_update/<int:id>/', views.supplier_update,name='supplier_update'),
    path('supplier_delete/<int:id>/', views.supplier_delete,name='supplier_delete'),

    # URLs de categorías
    path('category_list/', views.category_List,name='category_list'),
    path('category_create/', views.category_create,name='category_create'),
    path('category_update/<int:id>/', views.category_update,name='category_update'),
    path('category_delete/<int:id>/', views.category_delete,name='category_delete'),
]
