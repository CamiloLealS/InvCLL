# Generated by Django 5.0.1 on 2024-01-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0005_alter_equipo_mantencion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='mantencion',
            field=models.CharField(default='-', max_length=20, verbose_name='Fecha Mantención'),
        ),
    ]