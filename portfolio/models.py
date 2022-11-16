from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField (max_length=150,verbose_name='Nombre de la Imagen')
    image = models.ImageField(verbose_name='Imagen', upload_to='portfolio')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Imagen de Trabajo'
        verbose_name_plural = 'Imagenes de Trabajos'
        ordering = ['-created']

    def __str__(self):
        return self.title
