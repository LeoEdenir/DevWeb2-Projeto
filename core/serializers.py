from django.contrib.auth.hashers import make_password
from rest_framework.fields import CharField, SerializerMethodField

from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from core.models import Categoria, Tarefa, ExecucaoTarefa


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UsuarioSerializer, self).create(validated_data)


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ExecucaoTarefaSerializer(ModelSerializer):
    class Meta:
        model = ExecucaoTarefa
        fields = '__all__'


class ExecucaoTarefaDetailSerializer(ModelSerializer):

    class Meta:
        model = ExecucaoTarefa
        fields = '__all__'
        depth = 2


class ExecucaoTarefaSoftSerializer(ModelSerializer):
    usuario = CharField(source='usuario.username')
    status = SerializerMethodField()

    class Meta:
        model = ExecucaoTarefa
        fields = ('id', 'usuario', 'status')

    def get_status(self, instance):
        return instance.get_status_display()


class TarefaSerializer(ModelSerializer):
    execucoes_tarefa = ExecucaoTarefaSoftSerializer(read_only=True, many=True)

    class Meta:
        model = Tarefa
        fields = '__all__'
