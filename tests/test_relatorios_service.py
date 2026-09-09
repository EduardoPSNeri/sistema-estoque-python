from decimal import Decimal

from models.produto import Produto
from services.relatorios_service import (
    produto_mais_caro,
    produto_maior_quantidade,
    total_itens,
    valor_estoque,
)


def produtos_exemplo():
    return [
        Produto(1, "Teclado", 2, "100.00"),
        Produto(2, "Monitor", 1, "900.00"),
        Produto(3, "Mouse", 5, "50.00"),
    ]


def test_produto_mais_caro():
    assert produto_mais_caro(produtos_exemplo()).nome == "Monitor"


def test_produto_maior_quantidade():
    assert produto_maior_quantidade(produtos_exemplo()).nome == "Mouse"


def test_valor_total_estoque():
    assert valor_estoque(produtos_exemplo()) == Decimal("1350.00")


def test_total_itens():
    assert total_itens(produtos_exemplo()) == 8


def test_relatorios_com_lista_vazia():
    assert produto_mais_caro([]) is None
    assert produto_maior_quantidade([]) is None
    assert valor_estoque([]) == Decimal("0.00")
    assert total_itens([]) == 0
