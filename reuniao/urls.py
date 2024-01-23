# reuniao/urls.py
from django.urls import path
from .views import EncaminhamentoListView
from . import views

urlpatterns = [
    path('encaminhamentos/', EncaminhamentoListView.as_view(), name='lista_encaminhamentos'),
    #path('', views.post_list, name='post_list'),
]
