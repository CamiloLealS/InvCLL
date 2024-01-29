from typing import Any
from django import forms 
from django.forms import ModelForm
from .models import equipo

FORMATOS_FECHA = ('%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%m/%d/%Y', '%d/%m/%y', '%d/%m/%Y')

class equipoForm(ModelForm):
    mantencion = forms.DateField(input_formats=FORMATOS_FECHA)
    
    class Meta:
        model = equipo

        fields = ['ubicacion','tipo','ip','mac','mantencion']
        
        widgets = {
            'ubicacion' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : ''
               } 
            ),
            'tipo' : forms.Select(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : ''
               } 
            ),
            'ip' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : ''
               } 
            ),
            'mac' : forms.TextInput(
               attrs = {
                   'class' : 'form-control',
                   'placeholder' : ''
               } 
            ),
            'estadoMant':forms.TextInput(
                attrs= {
                    'class' : 'form-control',
                    'placeholder' : ''
                }
            )
        }

        def save(self, commit = True):
            equipo = super().save(commit = False)
            equipo.tipo = equipo.tipo.upper()
            
            if commit:
                equipo.save()
            
            return equipo

