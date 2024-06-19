from django import forms
from app_contatos.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'