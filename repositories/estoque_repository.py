from __future__ import annotations

import json
from pathlib import Path

from models.produto import Produto


class PersistenciaError(RuntimeError):
    """Erro ao ler ou gravar os dados do estoque."""


class EstoqueRepository:
    def __init__(self, caminho: str | Path | None = None) -> None:
        if caminho is None:
            caminho = (
                Path(__file__).resolve().parent.parent
                / "data"
                / "estoque.json"
            )

        self.caminho = Path(caminho)

    def carregar(self) -> list[Produto]:
        if not self.caminho.exists():
            return []

        try:
            with self.caminho.open("r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except json.JSONDecodeError as exc:
            raise PersistenciaError(
                f"O arquivo de estoque está com JSON inválido: {self.caminho}"
            ) from exc
        except OSError as exc:
            raise PersistenciaError(
                f"Não foi possível ler o arquivo de estoque: {self.caminho}"
            ) from exc

        if not isinstance(dados, list):
            raise PersistenciaError(
                "O arquivo de estoque deve conter uma lista de produtos."
            )

        produtos: list[Produto] = []

        for indice, item in enumerate(dados, start=1):
            try:
                if not isinstance(item, dict):
                    raise ValueError("O registro não é um objeto JSON.")
                produtos.append(Produto.from_dict(item))
            except (ValueError, TypeError, KeyError) as exc:
                raise PersistenciaError(
                    f"Registro inválido na posição {indice} do arquivo de estoque."
                ) from exc

        return produtos

    def salvar(self, produtos: list[Produto]) -> None:
        try:
            self.caminho.parent.mkdir(parents=True, exist_ok=True)

            with self.caminho.open("w", encoding="utf-8") as arquivo:
                json.dump(
                    [produto.to_dict() for produto in produtos],
                    arquivo,
                    indent=2,
                    ensure_ascii=False,
                )
        except OSError as exc:
            raise PersistenciaError(
                f"Não foi possível salvar o estoque em: {self.caminho}"
            ) from exc
