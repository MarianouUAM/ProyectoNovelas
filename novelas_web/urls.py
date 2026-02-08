from django.contrib import admin
from django.urls import path
from catalogo.views import inicio, detalle, buscar_novelas
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    
    # Ruta oficial
    path('novela/<int:id>/', detalle, name='detalle'), 
    
    # NUEVA RUTA DE RESPALDO: Para evitar el error 404 del buscador
    path('detalle/<int:id>/', detalle), 
    
    path('buscar_ajax/', buscar_novelas, name='buscar_ajax'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)