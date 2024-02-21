# Generated by Django 4.2.6 on 2024-02-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0012_equipo_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='licencia',
            field=models.CharField(default='-', max_length=35, verbose_name='Licencia Windows'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='link',
            field=models.URLField(default='-', verbose_name='URL impresora'),
        ),
    ]