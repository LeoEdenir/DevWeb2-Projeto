from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core import views

router = DefaultRouter()
router.register('usuarios', views.UsuarioViewSet)
router.register('categorias', views.CategoriaViewSet)
router.register('tarefa', views.TarefaViewSet)
router.register('execucao-tarefa', views.ExecucaoTarefaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
