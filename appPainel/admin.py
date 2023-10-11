# bibliotecas
from django.contrib import admin
from django.forms import inlineformset_factory
from django.http import HttpResponse
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
# import csv
# Modelos
from .models import Eixo, Programa, Acao, Secretaria, Orgao, Responsavel, Municipio, Iniciativa, Monitoramento, Etapa, MonitoramentoEtapa, Fontes, FontesIniciativa, Produto, ProdutosIniciativa

admin.site.site_header = 'Painel de Controle' # Muda do site Admin

# Eixos - Formulário #
@admin.register(Eixo) # chama diretamente
class EixoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("eixo_estrategico_cd", "eixo_estrategico",)

# Programas - Formulário #
@admin.register(Programa) # chama diretamente
class EixoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("programa", "programa_cd",)

# Ações - Formulário #

@admin.register(Acao) # chama diretamente
class AcaoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("programa", "acao",)
    list_filter = ("programa",) # cria filtros
    # search_fields = ("iniciativa", "status",)

# Secretaria - Formulário #
class SecretariaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("secretaria",)

admin.site.register(Secretaria, SecretariaAdmin)

# Órgão - Formulário #
class OrgaoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("secretaria",)
admin.site.register(Orgao, OrgaoAdmin)

# Reponsável - Formulário #
class ResponsavelAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("nome", "secretaria",)

admin.site.register(Responsavel, ResponsavelAdmin)

# Município

@admin.register(Municipio) # chama diretamente
class MunicipioAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    ordering = ('nome',)
    list_display = ("codigo", "nome",)
    list_display_links = None
    list_filter = ("nome",) # cria filtros
    search_fields = ("codigo", "nome",)

# Iniciativa #
class FonteIniciativaInline(admin.StackedInline):  # ou admin.StackedInline
    model = FontesIniciativa
    extra = 0
    
class ProdutoIniciativaInline(admin.StackedInline):  # ou admin.StackedInline
    model = ProdutosIniciativa
    extra = 0

class EtapaInline(admin.StackedInline):  # ou admin.StackedInline
    model = Etapa
    extra = 0

#@admin.register(Iniciativa)
class IniciativaAdmin(ImportExportModelAdmin):
    model = Iniciativa
    inlines = [FonteIniciativaInline, ProdutoIniciativaInline, EtapaInline]
    list_display = ['acao', 'iniciativa']

admin.site.register(Iniciativa, IniciativaAdmin)

@admin.register(Fontes)
class FontesAdmin(ImportExportModelAdmin):
    list_display = ('fonte_cd',)

#@admin.register(ProdutosIniciativa)
#class ProdutosIniciativaAdmin(admin.ModelAdmin):
#    pass

@admin.register(Produto)
class ProdutoAdmin(ImportExportModelAdmin):
    list_display = ('produto_nm',)

# Monitoramento #
@admin.register(Monitoramento) # chama diretamente
class MonitoramentoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("iniciativa",)
    #list_editable = ("status", "execucao_fisica",) # permite editar do preview
    #list_filter = ("status",) # cria filtros
    # search_fields = ("iniciativa", "status",)

# Etapa #
# admin.site.register(Etapa)

# Monitoramento Etapa#
@admin.register(MonitoramentoEtapa) # chama diretamente
class MonitoramentoEtapaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("etapa", "status", "execucao_fisica",)
    list_editable = ("status", "execucao_fisica",) # permite editar do preview
    list_filter = ("status",) # cria filtros
    # search_fields = ("iniciativa", "status",)
# admin.site.register(Monitoramento, MonitoramentoAdmin) sintaxe sem @ e com .site