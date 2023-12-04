# bibliotecas
from django.contrib import admin
from django.forms import inlineformset_factory
from django.http import HttpResponse
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin
# import csv
# Modelosl
from .models import Ano, Tema, Tipo, Status, TipoPrograma, TipoAcao, Eixo, Programa, Acao, Secretaria, Orgao, Responsavel, Municipio, Meta, Monitoramento, Etapa, Subetapa, MonitoramentoEtapa, MonitoramentoSubetapa, Fontes, FontesMeta, Produto, ProdutosMeta, ProdutosEtapa

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from django import forms

from django.utils.translation import gettext_lazy as _
from django.forms import BaseInlineFormSet, ModelForm

from django.db import models

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
   list_display = ("meta", "status", "execucao_fisica",)
   list_editable = ("status", "execucao_fisica",) # permite editar do preview
   list_filter = ("meta", "status",) # cria filtros

### Monitoramento Etapa ###
class MonitoramentoSubetapaInLine(admin.StackedInline):  # ou admin.StackedInline
        model = MonitoramentoSubetapa
        extra = 0

@admin.register(MonitoramentoEtapa) # chama diretamente
class MonitoramentoEtapaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    
    #inlines = [MonitoramentoSubetapaInLine]

    list_display = ("etapa", "meta", "status", "execucao_fisica",)
    list_editable = ("meta", "status", "execucao_fisica",) # permite editar do preview
    list_filter = ("meta", "status",) # cria filtros

    change_form_template = "admin/add_form.html"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "etapa":
        
            meta_value = request.GET.getlist('meta')
            first_meta_value = meta_value[0] if meta_value else int(1)
            meta_id = int(first_meta_value)  

            if meta_value:
            # Filtrar o queryset com base no valor do campo "meta"
                kwargs["queryset"] = Etapa.objects.filter(meta=meta_id)
            else:
                kwargs["queryset"] = Etapa.objects.filter(meta=1)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['meta', 'etapa']
        return []
    
    fieldsets = (
        ('Geral', {
            'fields': ('meta', 'etapa', 'status', 'execucao_fisica', 'data_inicio_planejado', 'data_inicio_atualizado', 'data_termino_planejado', 'data_termino_atualizado', 'observacao', 'link_fotos', 'link_repositorio'),
        }),
    )
    
### Monitoramento Etapa ###
#@admin.register(MonitoramentoSubetapa) # chama diretamente
#class MonitoramentoEtapaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
#    list_display = ("subetapa",)
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

#### CAMPO CUSTOMIZADO
#class ChildModelForm(forms.ModelForm):
#    class Meta:
#        model = MonitoramentoSubetapa
#        fields = '__all__'

#    parent = forms.ModelChoiceField(
#        queryset=MonitoramentoEtapa.objects.all(),
#        widget=forms.Select(attrs={'style': 'width: 200px;'}),  # Adjust the style as needed
#        label='Select Parent'
#    )

@admin.register(MonitoramentoSubetapa)
class MonitoramentoSubetapaAdmin(ImportExportModelAdmin):
    list_display = ('meta_nome', 'etapa', 'subetapa_nome',)

    list_filter = ('etapa__meta', 'etapa__etapa') # cria filtros

    change_form_template = "admin/add_form_geral.html"

    def meta_nome(self, obj):
        # Retorna o nome da etapa associado à subetapa
        return obj.etapa.meta # Substitua 'meta' pelo nome correto do campo em MonitoramentoEtapa
    
    def subetapa_nome(self, obj):
        # Retorna o nome da etapa associado à subetapa
        return obj.subetapa.subetapa # Substitua 'meta' pelo nome correto do campo em MonitoramentoEtapa

    meta_nome.short_description = 'Nome da Meta'
    subetapa_nome.short_description = 'Nome da Meta'

    fieldsets = (
        ('Geral', {
            'fields': ('subetapa', 'data_inicio_planejado', 'data_inicio_atualizado', 'data_termino_planejado', 'data_termino_atualizado'),
        }),
    )