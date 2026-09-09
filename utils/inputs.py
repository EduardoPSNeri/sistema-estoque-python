from decimal import Decimal, InvalidOperation


def ler_int_positivo(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem).strip())
        except ValueError:
            print("Digite um número inteiro válido.")
            continue

        if valor <= 0:
            print("O valor deve ser maior que zero.")
            continue

        return valor


def ler_int_nao_negativo(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem).strip())
        except ValueError:
            print("Digite um número inteiro válido.")
            continue

        if valor < 0:
            print("O valor não pode ser negativo.")
            continue

        return valor


def ler_decimal_nao_negativo(mensagem: str) -> Decimal:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")

        try:
            valor = Decimal(entrada).quantize(Decimal("0.01"))
        except (InvalidOperation, ValueError):
            print("Digite um valor monetário válido.")
            continue

        if valor < 0:
            print("O valor não pode ser negativo.")
            continue

        return valor


def ler_texto_obrigatorio(mensagem: str) -> str:
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Este campo é obrigatório.")


def ler_int_nao_negativo_opcional(mensagem: str) -> int | None:
    while True:
        entrada = input(mensagem).strip()

        if not entrada:
            return None

        try:
            valor = int(entrada)
        except ValueError:
            print("Digite um número inteiro válido ou deixe em branco.")
            continue

        if valor < 0:
            print("O valor não pode ser negativo.")
            continue

        return valor


def ler_decimal_nao_negativo_opcional(mensagem: str) -> Decimal | None:
    while True:
        entrada = input(mensagem).strip().replace(",", ".")

        if not entrada:
            return None

        try:
            valor = Decimal(entrada).quantize(Decimal("0.01"))
        except (InvalidOperation, ValueError):
            print("Digite um valor monetário válido ou deixe em branco.")
            continue

        if valor < 0:
            print("O valor não pode ser negativo.")
            continue

        return valor
