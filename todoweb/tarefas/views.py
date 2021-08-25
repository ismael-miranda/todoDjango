from django.shortcuts import render
from django.urls import reverse
from todoweb.tarefas.forms import TarefaForm
from django.http import HttpResponseRedirect


def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            return render(request, 'tarefas/home.html', {'form': form}, status=400)
    return render(request, 'tarefas/home.html')
