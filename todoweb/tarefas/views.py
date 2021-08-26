from django.shortcuts import render
from django.urls import reverse
from todoweb.tarefas.forms import TarefaForm
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
            return render(
                request,
                'tarefas/home.html',
                {'form': form, 'tarefas_pendentes': tarefas_pendentes},
                status=400
            )
    tarefas_pendentes = Tarefa.objects.filter(feita=False).all()
    return render(request, 'tarefas/home.html', {'tarefas_pendentes': tarefas_pendentes})
