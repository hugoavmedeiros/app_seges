# reuniao/urls.py
from django.urls import path
from .views import EncaminhamentoListView
from . import views

app_name = 'reuniao'

urlpatterns = [
    path('', views.index, name='index'),
    path('encaminhamentos/', EncaminhamentoListView.as_view(), name='lista_encaminhamentos'),
]
