from django.db import models

# Create your models here.
class Novela(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título de la Novela")
    descripcion = models.TextField(verbose_name="Sinopsis")
    imagen = models.ImageField(upload_to='portadas/', verbose_name="Portada")
    link_drive = models.URLField(verbose_name="Enlace a Google Drive")

    def __str__(self):
        return self.titulo
