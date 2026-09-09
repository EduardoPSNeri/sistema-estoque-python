from decimal import Decimal

import pytest

from models.produto import Produto


def test_cria_produto_valido():
    produto = Produto(1, "Teclado", 2, Decimal("100.00"))

    assert produto.codigo == 1
    assert produto.nome == "Teclado"
    assert produto.quantidade == 2
    assert produto.preco == Decimal("100.00")
    assert produto.valor_total == Decimal("200.00")


@pytest.mark.parametrize(
    ("codigo", "nome", "quantidade", "preco"),
    [
        (0, "Teclado", 1, "10.00"),
        (1, "", 1, "10.00"),
        (1, "Teclado", -1, "10.00"),
        (1, "Teclado", 1, "-0.01"),
    ],
)
def test_rejeita_produto_invalido(codigo, nome, quantidade, preco):
    with pytest.raises(ValueError):
        Produto(codigo, nome, quantidade, preco)


def test_atualizar_produto():
    produto = Produto(1, "Teclado", 2, "100.00")

    produto.atualizar(nome="Teclado Mecânico", quantidade=3, preco="150.50")

    assert produto.nome == "Teclado Mecânico"
    assert produto.quantidade == 3
    assert produto.preco == Decimal("150.50")


def test_atualizacao_invalida_nao_altera_estado_anterior():
    produto = Produto(1, "Teclado", 2, "100.00")

    with pytest.raises(ValueError):
        produto.atualizar(nome="")

    assert produto.nome == "Teclado"
