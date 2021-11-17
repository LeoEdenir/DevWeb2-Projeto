from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    data_limite = models.DateField()

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class ExecucaoTarefa(models.Model):

    class StatusTarefa(models.IntegerChoices):
        ABERTO = 1, "Em Aberto"
        ANDAMENTO = 2, "Em Andamento"
        CONCLUIDO = 3, "Concluído"
        CANCELADO = 4, "Cancelado"

    tarefa = models.ForeignKey(Tarefa, on_delete=models.PROTECT, related_name='execucoes_tarefa')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='execucoes_tarefa')
    status = models.IntegerField(choices=StatusTarefa.choices, default=StatusTarefa.ABERTO)

    def __str__(self):
        return f"{self.tarefa} - {self.usuario} ({self.StatusTarefa.choices[self.status][1]})"
