from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse_lazy
from app_contatos.models import Contato
from app_contatos.forms import ContatoForm
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

# Create your views here.

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

class ListaContatos(ListView):
    template_name = 'lista_contatos.html'
    model = Contato
    queryset = Contato.objects.all()
    context_object_name = 'contatos'

class NovoContato(CreateView):
    template_name = 'novo_contato.html'
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('lista_contatos')

class AtualizarContato(UpdateView):
    model = Contato
    template_name = 'atualizar.html'
    fields = '__all__'
    context_object_name = 'contato'
    success_url = reverse_lazy('lista_contatos')

class VisualizarContato(DetailView):
    template_name = 'details.html'
    queryset = Contato.objects.all()
    fields = '__all__'
    context_object_name = 'contato'

class ExcluirContato(DeleteView):
    template_name = 'confirmar_exclusao.html'
    queryset = Contato.objects.all()
    success_url = reverse_lazy('lista_contatos')
    context_object_name = 'contato'