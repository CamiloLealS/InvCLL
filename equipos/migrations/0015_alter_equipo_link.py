# Generated by Django 4.2.6 on 2024-02-21 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0014_alter_equipo_proce_alter_equipo_ram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='link',
            field=models.CharField(default='-', max_length=200, verbose_name='URL impresora'),
        ),
    ]
