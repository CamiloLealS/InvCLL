from django.db import models
import datetime

# Create your models here.


class equipo(models.Model):
    id_equipo = models.AutoField(primary_key= True, null=False)
    nombre = models.CharField('Nombre de Equipo',max_length = 30, default = '')
    marca = models.CharField('Marca de Equipo', max_length = 15, default = '')
    modelo = models.CharField('Modelo de Equipo', max_length = 50, default = '')
    proce = models.CharField('Procesador',max_length = 40,blank = True ,default = '')
    ram = models.CharField('RAM',max_length = 15,blank = True, default = '')
    discos = (('-','-'),
              ('SSD','SSD'),
              ('HDD','HDD'))
    disco = models.CharField('Disco',max_length = 5, choices = discos ,blank = True, default = '-')
    ip = models.CharField('IP Equipo', max_length = 20, default = '')
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
                   ('INFORMATICA','INFORMATICA')"""
    ubicacion = models.CharField('Ubicación de Equipo', max_length=50, default ="")
    mac = models.CharField('MAC Equipo', max_length = 25, default = '')
    mantencion = models.CharField('Fecha Mantención', max_length = 20, default = '-')
    estados = (('PENDIENTE','PENDIENTE'),
               ('REALIZADA','REALIZADA'))
    estadoMant = models.CharField('Estado Mantención', choices = estados ,max_length = 12, default = 'PENDIENTE')

    def __str__(self) -> str:
        return self.ubicacion + '/' + self.tipo + ' ' +self.nombre