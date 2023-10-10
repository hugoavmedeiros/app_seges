# Painel de Controle (SEGES/SEPLAG)

O Painel de Controle é uma aplicação para coleta de dados desenvolvido pelo Instituto de Gestão Pública de Pernambuco, utilizando Django / Python. <br>

O ojetivo é coletar dados sobre projetos prioritários do Governo de Pernambuco, para subsidiar a tomada de decisão, o monitoramento e a avaliação de políticas públicas. <br>

A aplicação está baseada no painel administrativo do Django, customizado com o pacote Jazzmin (https://django-jazzmin.readthedocs.io/). 

## Modelos
https://github.com/hugoavmedeiros/painel_de_controle/blob/main/appPainel/models.py
<p> Os modelos são responsáveis pelos campos que vão ser montados tanto no banco quanto nos formulários </p>
<p>Cada modelo gera um dos formulários presentes na aplicação</p>
- Lista de Modelos
    - Eixo: informações sobre os objetivos estratégicos das metas monitoradas
    - Fontes: fontes orçamentárias dos recursos utilizados nas metas monitoradas
    - Produtos: produtos gerados com as atividades / a execução das metas prioritárias
    - Programa: programa orçamentário ao qual está vinculada a meta monitorada
    - Ação: ação orçamentária à qual está vinculada a meta monitorada
    - Secretaria: secretaria (Adm. Direta) responsável pela execução da meta monitorada
    - Órgão: órgão (Adm. Indireta) responsável pela execução da meta monitorada, quando couber
    - Município: municípios beneficiados pela meta monitorada
    - Responsável: pessoa responsável pela meta monitorada na secretaria ou órgão de execução
    - Iniciativa: dados sobre a meta monitorada
    - Etapa: dados sobre as etapas da obra monitorada
    - Monitoramento: dados do acompanhamento da meta monitorada
    - MonitoramentoEtapa: dados do acompanhamento das etapas da meta monitorada
    - FontesIniciativa: dados do relacionamento entre as metas e suas fontes de recursos (tabela inline)
    - ProdutosIniciativa: dados do relacionamento entre as metas e seus produtos (tabela inline)