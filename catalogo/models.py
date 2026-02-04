from django.db import models

# Create your models here.
class Novela(models.Model):
    TIPOS_NOVELA = [
        ('Novela Ligera', 'Novela Ligera (Japón)'),
        ('Web Novel', 'Web Novel (Corea)'),
        ('Novela China', 'Novela China (Wuxia/Xianxia)'),
        ('Otro', 'Otro'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título de la Novela")
    tipo = models.CharField(
        max_length=50, 
        choices=TIPOS_NOVELA, 
        default='Novela Ligera',
        verbose_name="Tipo de Novela"
    )
    genero = models.CharField(max_length=100, verbose_name="Género", default="Fantasía")
    
    descripcion = models.TextField(verbose_name="Sinopsis")
    imagen = models.ImageField(upload_to='portadas/', verbose_name="Portada")
    link_drive = models.URLField(verbose_name="Enlace a Google Drive")

    def __str__(self):
        return self.titulo