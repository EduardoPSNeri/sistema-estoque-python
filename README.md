# Sistema de Controle de Estoque em Python

Aplicação CLI desenvolvida em Python para gerenciamento de produtos em estoque, com persistência em JSON, regras de negócio separadas por camada e testes automatizados.

O projeto foi refatorado com foco em **organização, legibilidade, validação de dados, persistência segura e boas práticas de desenvolvimento back-end**.

## Funcionalidades

- Cadastro de produtos;
- listagem ordenada por código;
- busca por código;
- busca por nome;
- edição de produtos;
- exclusão de produtos;
- persistência automática em JSON após alterações;
- carregamento dos dados ao iniciar o sistema.

### Relatórios

- Produto mais caro;
- produto com maior quantidade;
- valor financeiro total do estoque;
- quantidade total de itens armazenados.

## Regras de negócio

Cada produto possui:

- código inteiro positivo e único;
- nome obrigatório;
- quantidade inteira maior ou igual a zero;
- preço maior ou igual a zero.

Valores monetários utilizam `Decimal`, evitando os problemas mais comuns de precisão associados a `float`.

## Arquitetura

```text
sistema-estoque-python/
│
├── models/
│   ├── __init__.py
│   └── produto.py
│
├── services/
│   ├── __init__.py
│   ├── estoque_service.py
│   └── relatorios_service.py
│
├── repositories/
│   ├── __init__.py
│   └── estoque_repository.py
│
├── utils/
│   ├── __init__.py
│   └── inputs.py
│
├── data/
│   └── .gitkeep
│
├── tests/
│   ├── test_produto.py
│   ├── test_estoque_service.py
│   ├── test_relatorios_service.py
│   └── test_estoque_repository.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Responsabilidade das camadas

**Model**
: representa a entidade `Produto`, valida seus próprios dados e realiza serialização.

**Services**
: concentram as regras de negócio de estoque e os cálculos dos relatórios.

**Repository**
: é responsável pela leitura e gravação do arquivo JSON.

**Utils**
: reúne funções de entrada e validação utilizadas pela interface de terminal.

**main.py**
: coordena o fluxo da aplicação e a interação com o usuário.

## Tecnologias

- Python 3.10+
- JSON
- `decimal.Decimal`
- `pathlib`
- Pytest
- Git / GitHub

Não há dependências de produção externas.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/EduardoPSNeri/sistema-estoque-python.git
cd sistema-estoque-python
```

Crie e ative um ambiente virtual.

### Windows / PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências de desenvolvimento:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

## Testes

Execute:

```bash
pytest -q
```

A suíte cobre:

- validações do model;
- cadastro com código único;
- bloqueio de código duplicado;
- busca;
- edição;
- exclusão;
- relatórios;
- casos com estoque vazio;
- persistência;
- arquivo inexistente;
- JSON inválido;
- registro malformado.

## Persistência

Os dados gerados pela aplicação são armazenados em:

```text
data/estoque.json
```

Esse arquivo é criado automaticamente e está no `.gitignore`, portanto dados locais de teste não são enviados ao GitHub.

A classe `EstoqueRepository` aceita um caminho alternativo, facilitando testes automatizados sem alterar dados reais.

## Principais melhorias da refatoração

- `Produto` deixou de fazer `print()` diretamente;
- validações da entidade foram centralizadas;
- preço passou a utilizar `Decimal`;
- edição deixou de alterar atributos diretamente no `main.py`;
- persistência foi movida para uma camada `repositories`;
- caminho do JSON deixou de depender da pasta em que o terminal foi aberto;
- erros de leitura e gravação passaram a ter tratamento explícito;
- registros JSON inválidos são detectados;
- operações de cadastro, edição e exclusão salvam automaticamente;
- funções passaram a possuir responsabilidades mais claras;
- suíte de testes foi ampliada;
- `requirements.txt` foi reduzido apenas à dependência realmente utilizada;
- README e links do repositório foram corrigidos.

## Possíveis evoluções futuras

Este projeto deve permanecer pequeno e focado em fundamentos de Python. Evoluções naturais, caso seja necessário criar uma segunda versão, seriam:

- SQLite;
- API REST com FastAPI;
- paginação e filtros;
- controle de entradas e saídas;
- histórico de movimentações.

Essas funcionalidades não são necessárias para o objetivo atual do projeto CLI.

## Autor

Desenvolvido por **Eduardo Neri** como projeto de estudo e portfólio.

GitHub: <https://github.com/EduardoPSNeri>
LinkedIn: <https://www.linkedin.com/in/eduardo-neri-96b3732a5/>
