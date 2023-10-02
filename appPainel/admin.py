# bibliotecas
from django.contrib import admin
from django.forms import inlineformset_factory
from django.http import HttpResponse
from import_export.admin import ImportExportActionModelAdmin
# import csv
# Modelos
from .models import Eixo, Programa, Acao, Secretaria, Orgao, Responsavel, Municipio, Iniciativa, Monitoramento, Etapa, MonitoramentoEtapa, Fontes, FontesIniciativa, ProdutosIniciativa

admin.site.site_header = 'Painel de Controle' # Muda do site Admin

# Eixos - Formulário #
@admin.register(Eixo) # chama diretamente
class EixoAdmin(ImportExportActionModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("eixo_estrategico_cd", "eixo_estrategico",)

# Programa - Formulário #
admin.site.register(Programa)

# Ação #

@admin.register(Acao) # chama diretamente
class AcaoAdmin(ImportExportActionModelAdmin): # lista_display permite mostrar campos customizados
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
class MunicipioAdmin(ImportExportActionModelAdmin): # lista_display permite mostrar campos customizados
    ordering = ('nome',)
    list_display = ("codigo", "nome",)
    list_filter = ("nome",) # cria filtros
    # search_fields = ("iniciativa", "status",)

# Iniciativa #
class FonteIniciativaInline(admin.StackedInline):  # ou admin.StackedInline
    model = FontesIniciativa
    
class ProdutoIniciativaInline(admin.StackedInline):  # ou admin.StackedInline
    model = ProdutosIniciativa

@admin.register(Iniciativa)
class IniciativaAdmin(ImportExportActionModelAdmin):
    inlines = [FonteIniciativaInline, ProdutoIniciativaInline]
    list_display = ['acao', 'iniciativa']

@admin.register(Fontes)
class FontesIniciativaAdmin(admin.ModelAdmin):
    list_display = ('fonte_cd',)

#@admin.register(ProdutosIniciativa)
#class ProdutosIniciativaAdmin(admin.ModelAdmin):
#    pass

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