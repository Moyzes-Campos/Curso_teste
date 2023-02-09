from django.urls import path
from .views import CriarEmpresa, EditarEmpresa

urlpatterns = [
    path('novo', CriarEmpresa.as_view(), name='criar_empresa'),
    path('editar/<int:pk>', EditarEmpresa.as_view(), name='editar_empresa'),
]
