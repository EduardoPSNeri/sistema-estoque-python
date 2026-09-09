from models.produto import Produto
from repositories.estoque_repository import EstoqueRepository, PersistenciaError
from services.estoque_service import (
    buscar_por_codigo,
    buscar_por_nome,
    cadastrar_produto,
    editar_produto,
    excluir_produto,
)
from services.relatorios_service import (
    produto_mais_caro,
    produto_maior_quantidade,
    total_itens,
    valor_estoque,
)
from utils.inputs import (
    ler_decimal_nao_negativo,
    ler_decimal_nao_negativo_opcional,
    ler_int_nao_negativo,
    ler_int_nao_negativo_opcional,
    ler_int_positivo,
    ler_texto_obrigatorio,
)


def exibir_menu() -> None:
    print("\n=== SISTEMA DE CONTROLE DE ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Editar produto")
    print("5 - Excluir produto")
    print("6 - Produto mais caro")
    print("7 - Produto com maior quantidade")
    print("8 - Valor total em estoque")
    print("9 - Total de itens")
    print("10 - Salvar e sair")


def listar_produtos(produtos: list[Produto]) -> None:
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    print("\n--- PRODUTOS CADASTRADOS ---")
    for produto in sorted(produtos, key=lambda item: item.codigo):
        print(produto)


def salvar(repository: EstoqueRepository, produtos: list[Produto]) -> bool:
    try:
        repository.salvar(produtos)
        return True
    except PersistenciaError as exc:
        print(f"\nErro ao salvar: {exc}")
        return False


def cadastrar(produtos: list[Produto], repository: EstoqueRepository) -> None:
    codigo = ler_int_positivo("Código: ")
    nome = ler_texto_obrigatorio("Nome: ")
    quantidade = ler_int_nao_negativo("Quantidade: ")
    preco = ler_decimal_nao_negativo("Preço: R$ ")

    try:
        produto = Produto(codigo, nome, quantidade, preco)
        cadastrar_produto(produtos, produto)
    except ValueError as exc:
        print(f"\nNão foi possível cadastrar: {exc}")
        return

    if salvar(repository, produtos):
        print("\nProduto cadastrado com sucesso!")


def buscar(produtos: list[Produto]) -> None:
    print("\n1 - Buscar por código")
    print("2 - Buscar por nome")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        codigo = ler_int_positivo("Código: ")
        produto = buscar_por_codigo(produtos, codigo)
    elif opcao == "2":
        nome = ler_texto_obrigatorio("Nome: ")
        produto = buscar_por_nome(produtos, nome)
    else:
        print("\nOpção de busca inválida.")
        return

    if produto is None:
        print("\nProduto não encontrado.")
        return

    print(f"\n{produto}")


def editar(produtos: list[Produto], repository: EstoqueRepository) -> None:
    codigo = ler_int_positivo("Código do produto: ")
    produto = buscar_por_codigo(produtos, codigo)

    if produto is None:
        print("\nProduto não encontrado.")
        return

    print(f"\nAtual: {produto}")
    print("Deixe o campo em branco para manter o valor atual.")

    novo_nome = input(f"Novo nome [{produto.nome}]: ").strip() or None
    nova_quantidade = ler_int_nao_negativo_opcional(
        f"Nova quantidade [{produto.quantidade}]: "
    )
    novo_preco = ler_decimal_nao_negativo_opcional(
        f"Novo preço [R$ {produto.preco:.2f}]: "
    )

    try:
        editar_produto(
            produtos,
            codigo,
            nome=novo_nome,
            quantidade=nova_quantidade,
            preco=novo_preco,
        )
    except (LookupError, ValueError) as exc:
        print(f"\nNão foi possível editar: {exc}")
        return

    if salvar(repository, produtos):
        print("\nProduto atualizado com sucesso!")


def excluir(produtos: list[Produto], repository: EstoqueRepository) -> None:
    codigo = ler_int_positivo("Código do produto: ")

    try:
        produto = excluir_produto(produtos, codigo)
    except LookupError as exc:
        print(f"\n{exc}")
        return

    if salvar(repository, produtos):
        print(f"\nProduto '{produto.nome}' excluído com sucesso!")


def main() -> None:
    repository = EstoqueRepository()

    try:
        produtos = repository.carregar()
    except PersistenciaError as exc:
        print(f"Erro ao carregar o estoque: {exc}")
        print("O sistema será iniciado com o estoque vazio.")
        produtos = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar(produtos, repository)

        elif opcao == "2":
            listar_produtos(produtos)

        elif opcao == "3":
            buscar(produtos)

        elif opcao == "4":
            editar(produtos, repository)

        elif opcao == "5":
            excluir(produtos, repository)

        elif opcao == "6":
            produto = produto_mais_caro(produtos)
            print(f"\n{produto}" if produto else "\nNenhum produto cadastrado.")

        elif opcao == "7":
            produto = produto_maior_quantidade(produtos)
            print(f"\n{produto}" if produto else "\nNenhum produto cadastrado.")

        elif opcao == "8":
            print(f"\nValor total em estoque: R$ {valor_estoque(produtos):.2f}")

        elif opcao == "9":
            print(f"\nTotal de itens: {total_itens(produtos)}")

        elif opcao == "10":
            if salvar(repository, produtos):
                print("\nEstoque salvo. Até mais!")
                break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    main()
