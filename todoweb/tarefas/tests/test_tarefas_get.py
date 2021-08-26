# from django.test import Client
import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from todoweb.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_form_available(resposta):
    assertContains(resposta, '<form')


def test_btn_salvar_available(resposta):
    assertContains(resposta, '<button type="submit"')


@pytest.fixture
def lista_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Tarefa 1', feita=False),
        Tarefa(nome='Tarefa 2', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def resp_lista_tarefas(client, lista_tarefas_pendentes):
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_lista_tarefas_pendents_present(resp_lista_tarefas, lista_tarefas_pendentes):
    for tarefa in lista_tarefas_pendentes:
        assertContains(resp_lista_tarefas, tarefa.nome)
