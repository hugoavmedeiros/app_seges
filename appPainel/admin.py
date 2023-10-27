# bibliotecas
from django.contrib import admin
from django.forms import inlineformset_factory
from django.http import HttpResponse
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
# import csv
# Modelosl
from .models import Ano, Tema, Tipo, Status, TipoPrograma, TipoAcao, Eixo, Programa, Acao, Secretaria, Orgao, Responsavel, Municipio, Meta, Monitoramento, Etapa, Subetapa, MonitoramentoEtapa, MonitoramentoSubetapa, Fontes, FontesMeta, Produto, ProdutosMeta, ProdutosEtapa

admin.site.site_header = 'Painel de Controle' # Muda do site Admin

######### FORMULÁRIOS DE APOIO ##########

# Temas - Formulário #
@admin.register(Tema) # chama diretamente
class TemaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("tema_nm",)

# Tipos - Formulário #
@admin.register(Tipo) # chama diretamente
class TipoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("tipo_nm",)

# Status - Formulário #
@admin.register(Status) # chama diretamente
class StatusAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("status_nm",)

# Ano - Formulário #
@admin.register(Ano) # chama diretamente
class AnoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("ano_nr",)

# TipoPrograma - Formulário #
@admin.register(TipoPrograma) # chama diretamente
class TipoProgramaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("tipo_programa_nm",)

# TipoAcao - Formulário #
@admin.register(TipoAcao) # chama diretamente
class TipoAcaoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("tipo_acao_nm",)

######### FORMULÁRIOS ORÇAMENTÁRIOS ##########

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

############ FORMULÁRIOS DE METAS ############
### Metas ###
class FonteMetaInline(admin.StackedInline):  # ou admin.StackedInline
    model = FontesMeta
    extra = 0
    
class ProdutoMetaInline(admin.StackedInline):  # ou admin.StackedInline
    model = ProdutosMeta
    extra = 0

class MetaAdmin(ImportExportModelAdmin):
    model = Meta
    inlines = [FonteMetaInline, ProdutoMetaInline]
    list_display = ['acao', 'meta']

admin.site.register(Meta, MetaAdmin)

### Etapa ###
class ProdutoEtapaInline(admin.StackedInline):  # ou admin.StackedInline
    model = ProdutosEtapa
    extra = 0

class SubetapaInline(admin.StackedInline):  # ou admin.StackedInline
    model = Subetapa
    extra = 0

class EtapaAdmin(ImportExportModelAdmin):
    model = Etapa
    inlines = [ProdutoEtapaInline, SubetapaInline]
    list_display = ['meta', 'etapa']

admin.site.register(Etapa, EtapaAdmin)

### Subetapa ###

############ FORMULÁRIOS DE MONITORAMENTO ############
### Monitoramento ###
@admin.register(Monitoramento) # chama diretamente
class MonitoramentoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("meta",)
    #list_editable = ("status", "execucao_fisica",) # permite editar do preview
    #list_filter = ("status",) # cria filtros
    # search_fields = ("meta", "status",)

### Monitoramento Etapa ###
@admin.register(MonitoramentoEtapa) # chama diretamente
class MonitoramentoEtapaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("etapa", "status", "execucao_fisica",)
    list_editable = ("status", "execucao_fisica",) # permite editar do preview
    list_filter = ("status",) # cria filtros
    # search_fields = ("meta", "status",)
# admin.site.register(Monitoramento, MonitoramentoAdmin) sintaxe sem @ e com .site

### Monitoramento Etapa ###
@admin.register(MonitoramentoSubetapa) # chama diretamente
class MonitoramentoEtapaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("subetapa",)
    # search_fields = ("meta", "status",)
# admin.site.register(Monitoramento, MonitoramentoAdmin) sintaxe sem @ e com .site

############ MODELOS INLINE ############
### Produto ###
@admin.register(Produto)
class ProdutoAdmin(ImportExportModelAdmin):
    list_display = ('produto_nm',)

### Fontes ###
@admin.register(Fontes)
class FontesAdmin(ImportExportModelAdmin):
    list_display = ('fonte_cd', 'fonte_nm',)