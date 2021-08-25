# from django.test import Client
import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains


@pytest.fixture
def resposta(client):
    resp = client.get(reverse('tarefas:home'))
    return resp


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_form_available(resposta):
    assertContains(resposta, '<form')


def test_btn_salvar_available(resposta):
    assertContains(resposta, '<button type="submit"')
