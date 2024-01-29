from django.db import models
import datetime

# Create your models here.


class equipo(models.Model):
    id_equipo = models.AutoField(primary_key= True, null=False)
    ip = models.CharField('IP Equipo', max_length = 15, default = '')
    tipos = (("Tipo de Equipo","Tipo de Equipo"),
             ('COMPUTADOR','COMPUTADOR'),
             ('IMPRESORA','IMPRESORA'))
    tipo = models.CharField('Tipo de Equipo', max_length = 30 ,choices = tipos, default = "Tipo de Equipo" )
    """ubicaciones = (('Ubicación de Equipo','Ubicación de Equipo'),
                   ('CM ADULTO','CM ADULTO'),
                   ('CM TRAUMATOLOGICO','CM TRAUMATOLOGICO'),
                   ('CM PEDIATRICO','CM PEDIATRICO'),
                   ('CM GERENCIAL','CM GERENCIAL'),
                   ('CM CERVANTES','CM CERVANTES'),
                   ('UNIDAD DE EXAMENES','UNIDAD DE EXAMENES'),
                   ('RESONANCIA','RESONANCIA'),
                   ('RAYOS','RAYOS'),
                   ('MAMOGRAFIA','MAMOGRAFIA'),
                   ('SCANNER','SCANNER'),
                   ('ELECTRO','ELECTRO'),
                   ('TOMA DE MUESTRAS','TOMA DE MUESTRAS'),
                   ('URGENCIAS','URGENCIAS'),
                   ('URGENCIAS RECEPCION','URGENCIAS RECEPCION'),
                   ('HOSPITALIZACION','HOSPITALIZACION'),
                   ('UTI','UTI'),
                   ('CONTABILIDAD','CONTABILIDAD'),
                   ('RRHH','RRHH'),
                   ('VACUNATORIO','VACUNATORIO'),
                   ('MANTENCION','MANTENCION'),
                   ('PABELLON','PABELLON'),
                   ('PRESUPUESTOS','PRESUPUESTOS'),
                   ('COBRANZA','COBRANZA'),
                   ('GERENCIA EUSEBIO LILLO','GERENCIA EUSEBIO LILLO'),
                   ('GERENCIA CERVANTES','GERENCIA CERVANTES'),
                   ('FICHEROS','FICHEROS'),
                   ('FONASA','FONASA'),
                   ('CALIDAD','CALIDAD'),
                   ('INFORMACIONES','INFORMACIONES'),
                   ('INFORMATICA','INFORMATICA'),
                   ('PABELLON HEMODINAMIA','PABELLON HEMODINAMIA'))"""
    ubicacion = models.CharField('Ubicación de Equipo', max_length=50, default ="")
    mac = models.CharField('MAC Equipo', max_length = 20, default = '')
    mantencion = models.DateField(['%d%m/%Y'])
    estadoMant = models.CharField('Estado Mantención',max_length = 12, default = 'PENDIENTE')

    def __str__(self) -> str:
        return self.ubicacion + '/' + self.tipo + ' ' +self.ip