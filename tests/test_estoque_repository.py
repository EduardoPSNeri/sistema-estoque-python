import json

import pytest

from models.produto import Produto
from repositories.estoque_repository import EstoqueRepository, PersistenciaError


def test_salvar_e_carregar_estoque(tmp_path):
    caminho = tmp_path / "estoque.json"
    repository = EstoqueRepository(caminho)
    produtos = [
        Produto(1, "Teclado", 2, "100.00"),
        Produto(2, "Mouse", 3, "50.00"),
    ]

    repository.salvar(produtos)
    carregados = repository.carregar()

    assert [produto.to_dict() for produto in carregados] == [
        produto.to_dict() for produto in produtos
    ]


def test_carregar_arquivo_inexistente_retorna_lista_vazia(tmp_path):
    repository = EstoqueRepository(tmp_path / "nao_existe.json")

    assert repository.carregar() == []


def test_json_invalido_gera_erro_de_persistencia(tmp_path):
    caminho = tmp_path / "estoque.json"
    caminho.write_text("{json inválido", encoding="utf-8")
    repository = EstoqueRepository(caminho)

    with pytest.raises(PersistenciaError):
        repository.carregar()


def test_registro_malformado_gera_erro_de_persistencia(tmp_path):
    caminho = tmp_path / "estoque.json"
    caminho.write_text(
        json.dumps([{"codigo": 1, "nome": "Teclado"}]),
        encoding="utf-8",
    )
    repository = EstoqueRepository(caminho)

    with pytest.raises(PersistenciaError):
        repository.carregar()
