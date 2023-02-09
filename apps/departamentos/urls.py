from django.urls import path
from .views import DepartamentoList, DepartamentoCreate, DepartamentoUpdate, DepartamentoDelete

urlpatterns = [
    path('list', DepartamentoList.as_view(), name='departamento_list'),
    path('novo', DepartamentoCreate.as_view(), name='departamento_create'),
    path('update/<int:pk>', DepartamentoUpdate.as_view(), name='departamento_update'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='departamento_delete'),
]
