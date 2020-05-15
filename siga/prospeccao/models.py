from django.db import models
from core.models import Servidor

# Create your models here.


class DesafioInovacao(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    aprendizado = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    servidor = models.ForeignKey(
        Servidor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.titulo


class InovacaoAberta(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    aprendizado = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    servidor = models.ForeignKey(
        Servidor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.titulo


class ReuniaoGrupoPesquisa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    aprendizado = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    servidor = models.ForeignKey(
        Servidor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.titulo


class ReuniaoEmpresa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    aprendizado = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    servidor = models.ForeignKey(
        Servidor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.titulo

    verbose_name_plural = "Desafios da Inovacao"  # pra que serve isso aqui


class AtendimentoEmpreendedor(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    aprendizado = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    servidor = models.ForeignKey(
        Servidor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Atendimentos ao Empreendedor"
