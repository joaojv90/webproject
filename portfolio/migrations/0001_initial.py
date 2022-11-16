# Generated by Django 4.1.3 on 2022-11-16 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Nombre de la Imagen')),
                ('image', models.ImageField(upload_to='portfolio', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'Imagen de Trabajo',
                'verbose_name_plural': 'Imagenes de Trabajos',
                'ordering': ['-created'],
            },
        ),
    ]