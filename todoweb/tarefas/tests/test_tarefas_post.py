import pytest
from django.urls import reverse
from todoweb.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})
    return resp


def test_tarefa_existe_bd(resposta):
    assert Tarefa.objects.exists()


def test_redirect_depois_salvamento(resposta, db):
    assert resposta.status_code == 302


@pytest.fixture
def resposta_dado_invalido(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome': ''})
    return resp


def test_tarefa_nao_existe_bd(resposta_dado_invalido):
    assert not Tarefa.objects.exists()


def test_pag_dados_invalidos(resposta_dado_invalido, db):
    assert resposta_dado_invalido.status_code == 400



