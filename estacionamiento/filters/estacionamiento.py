from django_filters import rest_framework as filters
from estacionamiento.models import LugaresOcupados

class LugaresOcupadosFilter(filters.FilterSet):
    class Meta:
        model = LugaresOcupados
        fields = (
            'fecha_inicio',
            'fecha_fin',
            'estacionamiento',
            'roles'
        )