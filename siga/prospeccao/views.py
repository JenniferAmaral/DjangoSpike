from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import DesafioInovacao
from .models import InovacaoAberta

# Desafios de Inovação


class DesafioInovacao(generic.ListView):
    model = DesafioInovacao
    context_object_name = 'desafioInovacao_list'
    template_name = 'prospeccao/desafioInovacao_list.html'


class DesafioInovacaoDetailView(generic.DetailView):
    model = DesafioInovacao


class DesafioInovacaoCreate(CreateView):
    model = DesafioInovacao
    fields = '__all__'
    success_url = reverse_lazy('desafioInovacao')


class DesafioInovacaoUpdate(UpdateView):
    model = DesafioInovacao
    fields = '__all__'
    success_url = reverse_lazy('desafioInovacao')


class DesafioInovacaoDelete(DeleteView):
    model = InovacaoAberta
    success_url = reverse_lazy('desafioInovacao')

# Ação de Inovação Aberta


class InovacaoAberta(generic.ListView):
    model = InovacaoAberta
    context_object_name = 'inovacaoAberta_list'
    template_name = 'prospeccao/inovacaoAberta_list.html'


class InovacaoAbertaDetailView(generic.DetailView):
    model = InovacaoAberta


class InovacaoAbertaCreate(CreateView):
    model = InovacaoAberta
    fields = '__all__'
    success_url = reverse_lazy('inovacaoAberta')


class InovacaoAbertaUpdate(UpdateView):
    model = InovacaoAberta
    fields = '__all__'
    success_url = reverse_lazy('inovacaoAberta')


class InovacaoAbertaDelete(DeleteView):
    model = InovacaoAberta
    success_url = reverse_lazy('inovacaoAberta')
