from decimal import Decimal

from models.produto import Produto


def codigo_existe(produtos: list[Produto], codigo: int) -> bool:
    return any(produto.codigo == codigo for produto in produtos)


def buscar_por_codigo(produtos: list[Produto], codigo: int) -> Produto | None:
    return next((produto for produto in produtos if produto.codigo == codigo), None)


def buscar_por_nome(produtos: list[Produto], nome: str) -> Produto | None:
    termo = nome.strip().casefold()

    if not termo:
        return None

    return next(
        (produto for produto in produtos if produto.nome.casefold() == termo),
        None,
    )


def cadastrar_produto(produtos: list[Produto], produto: Produto) -> None:
    if codigo_existe(produtos, produto.codigo):
        raise ValueError(f"Já existe um produto com o código {produto.codigo}.")

    produtos.append(produto)


def editar_produto(
    produtos: list[Produto],
    codigo: int,
    *,
    nome: str | None = None,
    quantidade: int | None = None,
    preco: Decimal | int | float | str | None = None,
) -> Produto:
    produto = buscar_por_codigo(produtos, codigo)

    if produto is None:
        raise LookupError(f"Produto com código {codigo} não encontrado.")

    produto.atualizar(nome=nome, quantidade=quantidade, preco=preco)
    return produto


def excluir_produto(produtos: list[Produto], codigo: int) -> Produto:
    produto = buscar_por_codigo(produtos, codigo)

    if produto is None:
        raise LookupError(f"Produto com código {codigo} não encontrado.")

    produtos.remove(produto)
    return produto
