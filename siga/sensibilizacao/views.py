from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Palestra
from .models import Evento
from sensibilizacao.forms import CreatePalestraForm

# Palestras


def menu(request):
    return render(request, 'sensibilizacao/palestras/menu.html')


class PalestraListView(generic.ListView):
    model = Palestra
    context_object_name = 'palestras_list'
    template_name = 'sensibilizacao/palestras/palestra_list.html'


class PalestraDetailView(generic.DetailView):
    model = Palestra
    template_name = 'sensibilizacao/palestras/palestra_detail.html'


class PalestraCreate(CreateView):
    model = Palestra
    #fields = '__all__'
    success_url = reverse_lazy('palestras')
    form_class = CreatePalestraForm
    template_name = 'sensibilizacao/palestras/palestra_form.html'


class PalestraUpdate(UpdateView):
    model = Palestra
    fields = '__all__'
    success_url = reverse_lazy('palestras')
    template_name = 'sensibilizacao/palestras/palestra_update.html'


class PalestraDelete(DeleteView):
    model = Palestra
    success_url = reverse_lazy('palestras')
    template_name = 'sensibilizacao/palestras/palestra_confirm_delete.html'

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
