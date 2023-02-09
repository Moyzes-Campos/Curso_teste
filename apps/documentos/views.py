from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Documento


class DocumentList(ListView):
    model = Documento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Documento.objects.filter(empresa=empresa_logada)

