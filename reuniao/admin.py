#### BASE ####
from django.contrib import admin
from django.utils import timezone

#### LIBS ####
from import_export.admin import ImportExportModelAdmin

#### MODELOS ####
# Modelosl
from .models import Reuniao, Encaminhamento

#### Funções ####
class VencimentoProximoFilter(admin.SimpleListFilter):
    title = 'Vencimento Próximo'
    parameter_name = 'vencimento_proximo'

    def lookups(self, request, model_admin):
        return (
            ('7', 'Nos Próximos 7 Dias'),
            ('today', 'Hoje'),
        )

    def queryset(self, request, queryset):
        if self.value() == '7':
            return queryset.filter(prazo__gte=timezone.now(), prazo__lte=timezone.now() + timezone.timedelta(days=7))
        elif self.value() == 'today':
            return queryset.filter(prazo=timezone.now().date())

#### Formulários ####
@admin.register(Reuniao) # chama diretamente
class ReuniaoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = (
        "politica",
        "data",
        "numero",
        "assunto",
        )

@admin.register(Encaminhamento) # chama diretamente
class EncaminhamentoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = (
        "reuniao",
        'get_data',
        "assunto",
        "encaminhamento",
        "prazo",
        "devolutiva",
        )
    list_filter = (
        "reuniao__politica",
        "assunto", 
        "reuniao__data",
        VencimentoProximoFilter
        ) # cria filtros
    list_editable = (
        "encaminhamento",
        "prazo",
        "devolutiva",
        ) # permite editar do preview
    
    def get_data(self, obj):
        return obj.reuniao.data

    get_data.short_description = 'Data'