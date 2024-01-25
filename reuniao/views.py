#reuniao/views.py
from django.shortcuts import render

from django.views.generic import ListView
from .models import Encaminhamento, Reuniao
from django.http import HttpResponse
from .forms import EncaminhamentoFilterForm

def index(request):
    return render(request, 'reuniao/index.html')

class EncaminhamentoListView(ListView):
    model = Encaminhamento
    template_name = 'reuniao/lista_encaminhamentos.html'
    context_object_name = 'encaminhamentos'

    def get_queryset(self):
        queryset = super().get_queryset()
        reuniao_id = self.request.GET.get('reuniao', None)
        if reuniao_id:
            queryset = queryset.filter(reuniao_id=reuniao_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EncaminhamentoFilterForm(self.request.GET)
        context['reunioes'] = Reuniao.objects.all()
        return context