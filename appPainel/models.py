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
from multiselectfield import MultiSelectField

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

class Eixo(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    eixo_estrategico = models.CharField(max_length=255)
    eixo_estrategico_cd = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.eixo_estrategico + " " + self.eixo_estrategico_cd

class Programa(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    eixo_estrategico = models.ForeignKey(Eixo, on_delete=models.CASCADE)
    programa = models.CharField(max_length=255)
    programa_cd = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.programa + " " + self.programa_cd

class Acao(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    acao = models.CharField(max_length=255)
    acao_cd = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.acao + " " + self.acao_cd
    
    class Meta:
        verbose_name_plural = "Ações"

class Secretaria(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    secretaria = models.CharField(max_length=255)
    secretaria_cd = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.secretaria + " " + self.secretaria_cd
    
    class Meta:
        verbose_name_plural = "Secretarias"

class Orgao(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    orgao = models.CharField(max_length=255)
    orgao_cd = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.orgao + " | " + self.orgao_cd

    class Meta:
        verbose_name_plural = "Órgãos"   

class Responsavel(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=255)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Responsáveis"   

class Iniciativa(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    #eixo = models.ForeignKey(Eixo, on_delete=models.CASCADE)
    #programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, blank=True, null=True)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    gestor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    iniciativa = models.TextField(default='teste')
    iniciativa_cd = models.CharField(max_length=4)
    tipo = models.CharField(max_length=255, choices=tipo_lista)    
    tema = models.TextField()
    descricao = models.TextField()
    populacao = models.IntegerField()
    #municipio = MultiSelectField(choices=municipio_lista, default= 'Recife')
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.iniciativa

class Monitoramento(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    #eixo = models.ForeignKey(Eixo, on_delete=models.CASCADE)
    #programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    #acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    #secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=status_lista)
    data_inicio_planejado = models.DateTimeField(default=timezone.now)
    data_inicio_atualizado = models.DateTimeField(blank=True, null=True)
    data_termino_planejado = models.DateTimeField(default=timezone.now)
    data_termino_atualizado = models.DateTimeField(blank=True, null=True)
    execucao_fisica = models.DecimalField(
        max_digits=3, decimal_places=1, default=Decimal(0), validators=PERCENTAGE_VALIDATOR
        )
    observacao = models.TextField()
    link_fotos = models.URLField(max_length=500)
    link_repositorio = models.URLField(max_length=500)    
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Monitoramento"
        ordering = ("iniciativa",) # ordena pelo nome da iniciativa

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.status
    
class Etapa(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    #eixo = models.ForeignKey(Eixo, on_delete=models.CASCADE)
    #programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    iniciativa = models.ForeignKey(Iniciativa, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    etapa = models.TextField(default='teste')
    etapa_cd = models.CharField(max_length=4)
    tipo = models.CharField(max_length=255, choices=tipo_lista)    
    tema = models.TextField()
    descricao = models.TextField()
    populacao = models.IntegerField()
    #municipio = MultiSelectField(choices=municipio_lista, default= 'Recife')
    history = HistoricalRecords()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.etapa

class MonitoramentoEtapa(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    #eixo = models.ForeignKey(Eixo, on_delete=models.CASCADE)
    #programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    #acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    #secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=status_lista)
    data_inicio_planejado = models.DateTimeField(default=timezone.now)
    data_inicio_atualizado = models.DateTimeField(blank=True, null=True)
    data_termino_planejado = models.DateTimeField(default=timezone.now)
    data_termino_atualizado = models.DateTimeField(blank=True, null=True)
    execucao_fisica = models.DecimalField(
        max_digits=3, decimal_places=1, default=Decimal(0), validators=PERCENTAGE_VALIDATOR
        )
    observacao = models.TextField()
    link_fotos = models.URLField(max_length=500)
    link_repositorio = models.URLField(max_length=500)    
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Monitoramento"
        ordering = ("etapa",) # ordena pelo nome da iniciativa

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.status