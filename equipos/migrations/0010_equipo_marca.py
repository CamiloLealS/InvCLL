# Generated by Django 5.0.1 on 2024-02-01 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0009_alter_equipo_disco'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='marca',
            field=models.CharField(default='', max_length=15, verbose_name='Marca de Equipo'),
        ),
    ]
