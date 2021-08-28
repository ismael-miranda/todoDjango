import pytest
from django.urls import reverse
from todoweb.tarefas.models import Tarefa


@pytest.fixture
def apagar_tarefa(db):
    return Tarefa.objects.create(nome='Tarefa 1', feita=True)


@pytest.fixture
def resposta(client, apagar_tarefa):
    resp = client.post(
        reverse('tarefas:apagar', kwargs={'tarefa_id': apagar_tarefa.id})
    )
    return resp


def test_apagar_tarefa(resposta):
    assert not Tarefa.objects.exists()
