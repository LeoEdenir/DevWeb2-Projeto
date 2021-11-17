from rest_framework.viewsets import ModelViewSet

from core.models import Tarefa, ExecucaoTarefa
from core.serializers import TarefaSerializer, ExecucaoTarefaSerializer, ExecucaoTarefaDetailSerializer


class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


class ExecucaoTarefaViewSet(ModelViewSet):
    queryset = ExecucaoTarefa.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ExecucaoTarefaDetailSerializer

        return ExecucaoTarefaSerializer
