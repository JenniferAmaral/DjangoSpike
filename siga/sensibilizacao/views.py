from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Palestra
from .models import Evento

# Palestras


class PalestraListView(generic.ListView):
    model = Palestra
    context_object_name = 'palestras_list'
    # template_name = 'sensibilizacao/palestra_list.html'
    template_name = 'sensibilizacao/layouts/palestra.html'


class PalestraDetailView(generic.DetailView):
    model = Palestra


class PalestraCreate(CreateView):
    model = Palestra
    fields = '__all__'
    success_url = reverse_lazy('palestras')


class PalestraUpdate(UpdateView):
    model = Palestra
    fields = '__all__'
    success_url = reverse_lazy('palestras')


class PalestraDelete(DeleteView):
    model = Palestra
    success_url = reverse_lazy('palestras')

# Eventos


class EventoListView(generic.ListView):
    model = Evento
    context_object_name = 'eventos_list'
    template_name = 'sensibilizacao/evento_list.html'


class EventoDetailView(generic.DetailView):
    model = Evento


class EventoCreate(CreateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('eventos')


class EventoUpdate(UpdateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('eventos')


class EventoDelete(DeleteView):
    model = Evento
    success_url = reverse_lazy('eventos')
