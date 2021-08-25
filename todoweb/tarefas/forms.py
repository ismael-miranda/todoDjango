from django.forms import ModelForm
from todoweb.tarefas.models import Tarefa


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']
