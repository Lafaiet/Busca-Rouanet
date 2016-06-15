import django_filters
from models import Projeto

class ProjetoFilter(django_filters.FilterSet):
    class Meta:
        model = Projeto
        fields = {'PRONAC': ['exact'],
                  'municipio': ['icontains'],
                  'UF' : ['exact', 'icontains'],
                 }
