from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from core.serializers import UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer