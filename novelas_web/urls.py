from django.contrib import admin
from django.urls import path
from catalogo.views import inicio

# Estas 2 lineas son para configurar las imágenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'), # La ruta vacía '' significa la página principal
]

# Esto permite ver las fotos de portada mientras desarrollamos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)