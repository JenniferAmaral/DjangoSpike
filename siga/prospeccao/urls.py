from django.urls import path
from .views import *

urlpatterns = [
    path('desafioInovacao', DesafioInovacao.as_view(), name="desafioInovacao"),
    path('desafioInovacao/<int:pk>', DesafioInovacaoDetailView.as_view(),
         name='desafioInovacao-detail'),
    path('desafioInovacao/create/', DesafioInovacaoCreate.as_view(),
         name='desafioInovacao_create'),
    path('desafioInovacao/<int:pk>/update/',
         DesafioInovacaoUpdate.as_view(), name='desafioInovacao_update'),
    path('desafioInovacao/<int:pk>/delete/',
         DesafioInovacao.as_view(), name='desafioInovacao_delete'),
]
