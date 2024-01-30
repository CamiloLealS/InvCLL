from typing import Any
from django import forms 
from django.forms import ModelForm
from .models import equipo


class equipoForm(ModelForm):
    
    class Meta:
        model = equipo

        fields = ['ubicacion','tipo','nombre','modelo','proce','ram','ip','mac','mantencion','estadoMant']

        def save(self, commit = True):
            equipo = super().save(commit = False)
            equipo.tipo = equipo.tipo.upper()
            equipo.ubicacion = equipo.ubicacion.upper()
            if equipo.mantencion != '-':
                equipo.mantencion = equipo.mantencion

            if commit:
                equipo.save()
            
            return equipo

