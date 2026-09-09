from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


@dataclass(slots=True)
class Produto:
    codigo: int
    nome: str
    quantidade: int
    preco: Decimal

    def __post_init__(self) -> None:
        self.nome = self.nome.strip()
        self.preco = self._normalizar_preco(self.preco)
        self._validar()

    @staticmethod
    def _normalizar_preco(valor: Decimal | int | float | str) -> Decimal:
        try:
            return Decimal(str(valor)).quantize(Decimal("0.01"))
        except (InvalidOperation, ValueError, TypeError) as exc:
            raise ValueError("Preço inválido.") from exc

    def _validar(self) -> None:
        if self.codigo <= 0:
            raise ValueError("O código deve ser maior que zero.")

        if not self.nome:
            raise ValueError("O nome do produto é obrigatório.")

        if self.quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        if self.preco < 0:
            raise ValueError("O preço não pode ser negativo.")

    @property
    def valor_total(self) -> Decimal:
        return self.preco * self.quantidade

    def atualizar(
        self,
        *,
        nome: str | None = None,
        quantidade: int | None = None,
        preco: Decimal | int | float | str | None = None,
    ) -> None:
        nome_anterior = self.nome
        quantidade_anterior = self.quantidade
        preco_anterior = self.preco

        try:
            if nome is not None:
                self.nome = nome.strip()

            if quantidade is not None:
                self.quantidade = quantidade

            if preco is not None:
                self.preco = self._normalizar_preco(preco)

            self._validar()
        except ValueError:
            self.nome = nome_anterior
            self.quantidade = quantidade_anterior
            self.preco = preco_anterior
            raise

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": str(self.preco),
        }

    @classmethod
    def from_dict(cls, dados: dict) -> "Produto":
        campos = {"codigo", "nome", "quantidade", "preco"}
        ausentes = campos.difference(dados)

        if ausentes:
            raise ValueError(
                f"Registro de produto inválido. Campos ausentes: {', '.join(sorted(ausentes))}."
            )

        return cls(
            codigo=int(dados["codigo"]),
            nome=str(dados["nome"]),
            quantidade=int(dados["quantidade"]),
            preco=dados["preco"],
        )

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nome: {self.nome} | "
            f"Quantidade: {self.quantidade} | "
            f"Preço: R$ {self.preco:.2f} | "
            f"Total: R$ {self.valor_total:.2f}"
        )
