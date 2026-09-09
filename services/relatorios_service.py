from decimal import Decimal

from models.produto import Produto


def produto_mais_caro(produtos: list[Produto]) -> Produto | None:
    return max(produtos, key=lambda produto: produto.preco, default=None)


def produto_maior_quantidade(produtos: list[Produto]) -> Produto | None:
    return max(produtos, key=lambda produto: produto.quantidade, default=None)


def valor_estoque(produtos: list[Produto]) -> Decimal:
    return sum(
        (produto.valor_total for produto in produtos),
        start=Decimal("0.00"),
    )


def total_itens(produtos: list[Produto]) -> int:
    return sum(produto.quantidade for produto in produtos)
