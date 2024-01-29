from import_export import resources
from .models import equipo

class EquipoResource(resources.ModelResource):
    class Meta:
        model = equipo