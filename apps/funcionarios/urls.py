from django.urls import path
from .views import FuncionarioList, FuncionarioUpdate, FuncionarioDelete, FuncionarioCreate

urlpatterns = [
    path('', FuncionarioList.as_view(), name='funcionarios_list'),
    path('editar/<int:pk>', FuncionarioUpdate.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('criar', FuncionarioCreate.as_view(), name='criar_funcionario'),
]
