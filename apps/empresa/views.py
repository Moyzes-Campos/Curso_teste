from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from .models import Empresa


class CriarEmpresa(CreateView):
    model = Empresa
    fields = ['nome',]

    def form_valid(self, form):
        obj = form.save()  # Pega o objeto que está sendo salvo naquele formulário, que no caso é o nosso model Empresa
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj  # Salva a empresa no funcionario logado
        funcionario.save()
        return HttpResponse("Ok")


class EditarEmpresa(UpdateView):
    model = Empresa
    fields = ['nome', ]
