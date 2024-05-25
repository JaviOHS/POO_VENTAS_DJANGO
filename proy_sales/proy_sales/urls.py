from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views as core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core.home, name='home'),
    path('signup/', core.signup, name='signup'),
    path('logout/', core.signout, name='logout'),
    path('signin/', core.signin, name='signin'),
    path('', include('core.urls')),  # Elimina 'namespace'
    path('purchase/', include('purchase.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
