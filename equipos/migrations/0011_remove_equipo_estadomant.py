# Generated by Django 4.2.6 on 2024-02-14 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0010_equipo_marca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='estadoMant',
        ),
    ]
