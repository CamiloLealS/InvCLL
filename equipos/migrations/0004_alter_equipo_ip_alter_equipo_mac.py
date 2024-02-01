# Generated by Django 5.0.1 on 2024-01-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0003_alter_equipo_mantencion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='ip',
            field=models.CharField(default='', max_length=20, verbose_name='IP Equipo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='mac',
            field=models.CharField(default='', max_length=25, verbose_name='MAC Equipo'),
        ),
    ]