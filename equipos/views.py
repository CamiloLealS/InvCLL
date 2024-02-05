from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import equipoForm
from .models import equipo
from django.contrib import messages
import pandas as pd
from tablib import Dataset
from .resources import EquipoResource

# Create your views here.

def importarExcel(request):
    if request.method == 'POST':
        equipo_resource = EquipoResource
        data = Dataset()

        new_equipo = request.FILES['excel_uploaded']

        if not '.xls' in new_equipo.name:
            messages.info(request, 'Por favor utilizar un archivo excel ".xls".')
            return render(request, 'inventario/index.html')
        else:
            messages.info(request, 'Archivo subido correctamente.')

        dataset = pd.read_excel(new_equipo, header=None)

        for row in range(len(dataset)):
            ubi_eq = dataset.iloc[row,0].upper()
            nombre_eq = dataset.iloc[row, 1].upper()
            tipo_eq = dataset.iloc[row, 2].upper()
            marca = dataset.iloc[row, 3].upper()
            modelo_eq = dataset.iloc[row, 4]
            proce = dataset.iloc[row, 5]
            ram = dataset.iloc[row, 6].upper()
            disco = dataset.iloc[row, 7].upper()
            ip_equipo = dataset.iloc[row, 8]
            mac_eq = dataset.iloc[row, 9]
            mantencion_eq = dataset.iloc[row, 10]
            status = str(dataset.iloc[row, 11]).upper()
            if ip_equipo in equipo.objects.values_list('ip', flat=True).distinct():
                equipo.objects.filter(ip = ip_equipo).update(ubicacion = ubi_eq)
                equipo.objects.filter(ip = ip_equipo).update(mantencion = mantencion_eq)
                if status == '-':
                    if equipo.objects.get(ip = ip_equipo).estadoMant != 'REALIZADA':
                        equipo.objects.filter(ip = ip_equipo).update(estadoMant = 'PENDIENTE')
                    else:
                        equipo.objects.filter(ip = ip_equipo).update(estadoMant = 'REALIZADA')
                else:
                    equipo.objects.filter(ip = ip_equipo).update(estadoMant = status)
            else:
                if status == '-':
                    created = equipo.objects.update_or_create(
                        ubicacion = ubi_eq,
                        nombre = nombre_eq,
                        tipo = tipo_eq,
                        marca = marca,
                        modelo = modelo_eq,
                        proce = proce,
                        ram = ram,
                        disco = disco,
                        ip = ip_equipo,
                        mac = mac_eq,
                        mantencion = mantencion_eq,
                        estadoMant = 'PENDIENTE'
                        )
                else:
                    created = equipo.objects.update_or_create(
                        ubicacion = ubi_eq,
                        nombre = nombre_eq,
                        tipo = tipo_eq,
                        marca = marca,
                        modelo = modelo_eq,
                        proce = proce,
                        ram = ram,
                        disco = disco,
                        ip = ip_equipo,
                        mac = mac_eq,
                        mantencion = mantencion_eq,
                        estadoMant = status
                        )

        return redirect(to = 'index')
    return render(request, 'equipos/import.html')

        
class formEq(CreateView):
    model = equipo
    form_class = equipoForm
    template_name = 'equipos/registroEquipo.html'
    success_url = reverse_lazy('index')

def editEq(request, id_equipo):
    eq = equipo.objects.get(pk = id_equipo)
    form = equipoForm(request.POST, instance=eq)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(to='index')
        else:
            form = equipoForm(instance=eq)

    return render(request, 'equipos/editEquipo.html',{'form':form , 'eq': eq})     

def verEquipo(request, id_equipo):
    eq = equipo.objects.get(pk = id_equipo)

    return render(request, 'equipos/verEquipo.html',{'eq':eq})