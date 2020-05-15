
from django.urls import path
from .views import *

# app_name = 'sensibilizacao'

urlpatterns = [
    # Palestras
    path('palestras', PalestraListView.as_view(), name="palestras"),

    path('palestras/<int:pk>', PalestraDetailView.as_view(), name='palestra-detail'),

    path('palestras/create/', PalestraCreate.as_view(), name='palestra_create'),

    path('palestras/<int:pk>/update/',
         PalestraUpdate.as_view(), name='palestra_update'),

    path('palestras/<int:pk>/delete/',
         PalestraDelete.as_view(), name='palestra_delete'),

    # Eventos
    path('eventos', EventoListView.as_view(), name="eventos"),

    path('eventos/<int:pk>', EventoDetailView.as_view(), name='evento-detail'),

    path('eventos/create/', EventoCreate.as_view(), name='eventos_create'),

    path('eventos/<int:pk>/update/',
         EventoUpdate.as_view(), name='evento_update'),
    path('eventos/<int:pk>/delete/',
         EventoDelete.as_view(), name='evento_delete'),


]
