from django.contrib import admin
from .models import Eixo
from .models import Programa
from .models import Acao
from .models import Secretaria
from .models import Orgao
from .models import Responsavel
from .models import Municipio
from .models import Iniciativa
from .models import Monitoramento
from .models import Etapa
from .models import MonitoramentoEtapa
import csv
from django.http import HttpResponse

admin.site.register(Eixo)
admin.site.register(Programa)

admin.site.site_header = 'Painel de Controle' # Muda do site Admin

# Ação #

@admin.register(Acao) # chama diretamente
class AcaoAdmin(admin.ModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("programa", "acao",)
    list_filter = ("programa",) # cria filtros
    # search_fields = ("iniciativa", "status",)

# Secretaria #
admin.site.register(Secretaria)
admin.site.register(Orgao)

# Reponsável #
class ResponsavelAdmin(admin.ModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("nome", "secretaria",)

admin.site.register(Responsavel, ResponsavelAdmin)

@admin.register(Municipio) # chama diretamente
class MunicipioAdmin(admin.ModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("nome", "codigo",)
    list_filter = ("nome",) # cria filtros
    # search_fields = ("iniciativa", "status",)

# Iniciativa #
admin.site.register(Iniciativa)

# Monitoramento #
@admin.register(Monitoramento) # chama diretamente
class MonitoramentoAdmin(admin.ModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("iniciativa", "status", "execucao_fisica",)
    list_editable = ("status", "execucao_fisica",) # permite editar do preview
    list_filter = ("status",) # cria filtros
    # search_fields = ("iniciativa", "status",)

# Etapa #
admin.site.register(Etapa)

# Monitoramento Etapa#
@admin.register(MonitoramentoEtapa) # chama diretamente
class MonitoramentoEtapaAdmin(admin.ModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("etapa", "status", "execucao_fisica",)
    list_editable = ("status", "execucao_fisica",) # permite editar do preview
    list_filter = ("status",) # cria filtros
    # search_fields = ("iniciativa", "status",)
# admin.site.register(Monitoramento, MonitoramentoAdmin) sintaxe sem @ e com .site