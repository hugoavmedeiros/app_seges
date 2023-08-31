from django.db import models

# Create your models here.
from pickle import OBJ
from django.conf import settings
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

tipo_lista = (
    ('AÇÃO','AÇÃO'),
    ('AQUISIÇÃO', 'AQUISIÇÃO'),
    ('OBRA','OBRA'),
    ('PROGRAMA','PROGRAMA'),
    ('PROJETO DE LEI','PROJETO DE LEI'),
    ('PROJETO TÉCNICO','PROJETO TÉCNICO'),
    ('OUTROS','OUTROS'),
)

status_lista = (
    ('CANCELADA','CANCELADA'),
    ('CONCLUÍDA', 'CONCLUÍDA'),
    ('EM EXECUÇÃO','EM EXECUÇÃO'),
    ('EM FORMULAÇÃO','EM FORMULAÇÃO'),
    ('EM LICITAÇÃO','EM LICITAÇÃO'),
    ('LICITAÇÃO CONCLUÍDA','LICITAÇÃO CONCLUÍDA'),
    ('PARALISADA','PARALISADA'),
    ('PROJETO TÉCNICO EM ELABORAÇÃO','PROJETO TÉCNICO EM ELABORAÇÃO'),
    ('SUSPENSA','SUSPENSA'),
)

tipo_programa_lista = (
    ('Finalístico','Finalístico'),
    ('Gestão, Manutenção e Serviços ao Estado','Gestão, Manutenção e Serviços ao Estado'),
)

tipo_acao_lista = (
    ('Atividade','Atividade'),
    ('Operação Especial','Operação Especial'),
    ('Projeto','Projeto'),
)

class Eixo(models.Model):
    eixo_estrategico = models.CharField(_("Nome do Eixo"), max_length=255)
    eixo_estrategico_cd = models.CharField(_("Código do Eixo"), max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    descricao = models.TextField(verbose_name = _("Descrição"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.eixo_estrategico + " " + self.eixo_estrategico_cd

class Programa(models.Model):
    eixo_estrategico = models.ForeignKey(Eixo, on_delete=models.CASCADE, verbose_name = _("Nome do Eixo"))
    programa = models.CharField(verbose_name=_("Nome do Programa"), max_length=255)
    programa_cd = models.CharField(_("Código do Programa"), max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    tipo = models.CharField(max_length=255, choices=tipo_programa_lista, verbose_name = _("Tipo"))
    descricao = models.TextField(verbose_name = _("Descrição"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.programa + " " + self.programa_cd

class Acao(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, verbose_name = _("Nome do Programa"))
    acao = models.CharField(max_length=255, verbose_name = _("Nome da Ação"))
    acao_cd = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name = _("Código da Ação"))
    tipo = models.CharField(max_length=255, choices=tipo_acao_lista, verbose_name = _("Tipo"))
    descricao = models.TextField(verbose_name = _("Descrição"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.acao + " " + self.acao_cd
    
    class Meta:
        verbose_name_plural = "Ações"

class Secretaria(models.Model):
    secretaria = models.CharField(max_length=255, verbose_name = _("Nome da Secretaria"))
    secretaria_cd = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name = _("Código da Secretaria"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.secretaria + " " + self.secretaria_cd
    
    class Meta:
        verbose_name_plural = "Secretarias"

class Orgao(models.Model):
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, verbose_name = _("Nome da Secretaria"))
    orgao = models.CharField(max_length=255, verbose_name = _("Nome do Órgão"))
    orgao_cd = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name = _("Código do Órgão"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.orgao + " | " + self.orgao_cd

    class Meta:
        verbose_name_plural = "Órgãos"   

class Municipio(models.Model):
    nome = models.CharField(max_length=100, verbose_name = _("Nome do Município"))
    codigo = models.CharField(max_length=7, verbose_name = _("Código do Município"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Municípios"  

class Responsavel(models.Model):
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, verbose_name = _("Nome da Secretaria"))
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, blank=True, null=True, verbose_name = _("Nome do Órgão"))
    nome = models.CharField(max_length=255, verbose_name = _("Nome do(a) Responsável"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Responsáveis"   

class Iniciativa(models.Model):
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, verbose_name = _("Nome da Ação"))
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, verbose_name = _("Nome da Secretaria"))
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, blank=True, null=True, verbose_name = _("Nome do Órgão"))
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, verbose_name = _("Nome do(a) Responsável"))
    gestor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = _("Nome do(a) Gestor(a)"))
    iniciativa = models.TextField(default='teste', verbose_name = _("Nome da Iniciativa"))
    iniciativa_cd = models.CharField(max_length=4, verbose_name = _("Código da Iniciativa"))
    tipo = models.CharField(max_length=255, choices=tipo_lista, verbose_name = _("Tipo"))    
    tema = models.TextField(verbose_name = _("Tema"))
    descricao = models.TextField(verbose_name = _("Descrição"))
    populacao = models.IntegerField(verbose_name = _("População"))
    municipio = models.ManyToManyField(Municipio, default='Recife', verbose_name = _("Nome do Município"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.iniciativa

class Monitoramento(models.Model):
    iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE, verbose_name = _("Nome da Iniciativa"))
    status = models.CharField(max_length=255, choices=status_lista, verbose_name = _("Status"))
    data_inicio_planejado = models.DateTimeField(default=timezone.now, verbose_name = _("Data Planejada - Início"))
    data_inicio_atualizado = models.DateTimeField(blank=True, null=True, verbose_name = _("Data Atualizada - Início"))
    data_termino_planejado = models.DateTimeField(default=timezone.now, verbose_name = _("Data Planejada - Término"))
    data_termino_atualizado = models.DateTimeField(blank=True, null=True, verbose_name = _("Data Atualizada - Término"))
    execucao_fisica = models.DecimalField(
        max_digits=3, decimal_places=1, default=Decimal(0), validators=PERCENTAGE_VALIDATOR, verbose_name = _("Execução Física")
        )
    observacao = models.TextField(verbose_name = _("Observação"))
    link_fotos = models.URLField(max_length=500, verbose_name = _("Link de Fotos"))
    link_repositorio = models.URLField(max_length=500, verbose_name = _("Link do Repositório"))    
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Mon. de Iniciativas"
        ordering = ("iniciativa",) # ordena pelo nome da iniciativa

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.status
    
class Etapa(models.Model):
    iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE, verbose_name = _("Nome da Iniciativa"))
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, verbose_name = _("Nome do(a) Responsável"))
    etapa = models.TextField(default='teste', verbose_name = _("Nome da Etapa"))
    etapa_cd = models.CharField(max_length=4, verbose_name = _("Código da Etapa"))
    tipo = models.CharField(max_length=255, choices=tipo_lista,verbose_name = _("Tipo"))    
    tema = models.TextField(verbose_name = _("Tema"))
    descricao = models.TextField(verbose_name = _("Descrição"))
    populacao = models.IntegerField(verbose_name = _("População"))
    municipio = models.ManyToManyField(Municipio, default='Recife', verbose_name = _("Nome do Município"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.etapa

class MonitoramentoEtapa(models.Model):
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, verbose_name = _("Nome da Etapa"))
    status = models.CharField(max_length=255, choices=status_lista, verbose_name = _("Status"))
    data_inicio_planejado = models.DateTimeField(default=timezone.now, verbose_name = _("Data Planejada - Início"))
    data_inicio_atualizado = models.DateTimeField(blank=True, null=True, verbose_name = _("Data Atualizada - Início"))
    data_termino_planejado = models.DateTimeField(default=timezone.now, verbose_name = _("Data Planejada - Término"))
    data_termino_atualizado = models.DateTimeField(blank=True, null=True, verbose_name = _("Data Atualizada - Término"))
    execucao_fisica = models.DecimalField(
        max_digits=3, decimal_places=1, default=Decimal(0), validators=PERCENTAGE_VALIDATOR, verbose_name = _("Execução Física")
        )
    observacao = models.TextField(verbose_name = _("Observação"))
    link_fotos = models.URLField(max_length=500, verbose_name = _("Link de Fotos"))
    link_repositorio = models.URLField(max_length=500, verbose_name = _("Link de Repositório"))    
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Mon. de Etapas"
        ordering = ("etapa",) # ordena pelo nome da iniciativa

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.status