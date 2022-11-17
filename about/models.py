from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    names = models.CharField(max_length=150,verbose_name='Nombre y Apellido')
    position = models.CharField(max_length=50, verbose_name='Cargo')
    description = RichTextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name='Imagen',upload_to='about')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipo'
        ordering = ['-created']

    def __str__(self):
        return self.names
