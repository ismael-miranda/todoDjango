from django.shortcuts import render
from django.urls import reverse
from todoweb.tarefas.forms import TarefaForm, TarefaUpdateForm
from django.http import HttpResponseRedirect
from todoweb.tarefas.models import Tarefa


def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
            tarefas_feitas = Tarefa.objects.filter(feita=True).all()
            return render(
                request,
                'tarefas/home.html',
                {
                    'form': form,
                    'tarefas_pendentes': tarefas_pendentes,
                    'tarefas_feitas': tarefas_feitas
                },
                status=400
            )
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True).all()
    return render(
        request,
        'tarefas/home.html',
        {'tarefas_pendentes': tarefas_pendentes, 'tarefas_feitas': tarefas_feitas}
    )


def detalhe(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaUpdateForm(request.POST, instance=tarefa)
    if form.is_valid():
        form.save()

    return HttpResponseRedirect(reverse('tarefas:home'))
