import pytest

from models.produto import Produto
from services.estoque_service import (
    buscar_por_codigo,
    buscar_por_nome,
    cadastrar_produto,
    editar_produto,
    excluir_produto,
)


def test_cadastrar_produto():
    produtos = []
    produto = Produto(1, "Teclado", 2, "100.00")

    cadastrar_produto(produtos, produto)

    assert produtos == [produto]


def test_nao_cadastra_codigo_duplicado():
    produtos = [Produto(1, "Teclado", 2, "100.00")]

    with pytest.raises(ValueError, match="Já existe"):
        cadastrar_produto(produtos, Produto(1, "Mouse", 1, "50.00"))

    assert len(produtos) == 1


def test_buscar_por_codigo():
    produto = Produto(1, "Teclado", 2, "100.00")
    produtos = [produto]

    assert buscar_por_codigo(produtos, 1) is produto
    assert buscar_por_codigo(produtos, 99) is None


def test_buscar_por_nome_ignora_maiusculas_e_espacos():
    produto = Produto(1, "Teclado Mecânico", 2, "100.00")
    produtos = [produto]

    assert buscar_por_nome(produtos, "  teclado mecânico  ") is produto


def test_editar_produto():
    produtos = [Produto(1, "Teclado", 2, "100.00")]

    resultado = editar_produto(
        produtos,
        1,
        nome="Teclado Pro",
        quantidade=5,
        preco="200.00",
    )

    assert resultado.nome == "Teclado Pro"
    assert resultado.quantidade == 5
    assert str(resultado.preco) == "200.00"


def test_editar_produto_inexistente():
    with pytest.raises(LookupError):
        editar_produto([], 99, nome="Mouse")


def test_excluir_produto():
    produto = Produto(1, "Teclado", 2, "100.00")
    produtos = [produto]

    removido = excluir_produto(produtos, 1)

    assert removido is produto
    assert produtos == []


def test_excluir_produto_inexistente():
    with pytest.raises(LookupError):
        excluir_produto([], 99)
