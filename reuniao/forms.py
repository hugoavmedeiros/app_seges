# reuniao/forms.py
from django import forms
from .models import Reuniao

class EncaminhamentoFilterForm(forms.Form):
    reuniao = forms.ModelChoiceField(
        queryset=Reuniao.objects.all(), 
        empty_label='Todas as Reuniões',
        required=False
        )
