# 🛒 AppVendas

> Aplicativo desktop desenvolvido em Python para gerenciamento de clientes, produtos, controle de estoque e registro de vendas.

---

## 📋 Sumário
- [1. Visão Geral do Projeto](#1-visão-geral-do-projeto)
- [2. Mapeamento das Telas](#2-mapeamento-das-telas)
- [3. Fluxo de Navegação e Transição de Dados](#3-fluxo-de-navegação-e-transição-de-dados)
- [4. Estrutura de Código e Arquitetura](#4-estrutura-de-código-e-arquitetura)
- [5. Regras de Negócio e Validações](#5-regras-de-negócio-e-validações)
- [6. Instruções para Execução](#6-instruções-para-execução)

---

## 1. Visão Geral do Projeto

O **AppVendas** é um sistema modular desenvolvido para auxiliar pequenos comércios ou rotinas comerciais no registro e controle de dados operacionais. A aplicação centraliza o cadastro de clientes, gerenciamento de produtos e a realização de transações de vendas em uma interface intuitiva.

---

## 2. Mapeamento das Telas

Com base na estrutura de arquivos do projeto, as seguintes telas/módulos foram implementados:

| Módulo / Arquivo | Nome da Tela / Componente | Papel / Função no Aplicativo |
| :--- | :--- | :--- |
| `main.py` | Tela Principal / Inicializador | Ponto de entrada do sistema, responsável por inicializar a aplicação e integrar os módulos. |
| `tela_cliente.py` | Gerenciamento de Clientes | Interface para cadastro, edição, consulta e exclusão de clientes. |
| `tela_produto.py` | Gerenciamento de Produtos | Interface para controle de catálogo de produtos, preços e estoque. |
| `tela_venda.py` | Registro de Vendas | Interface para lançamento de vendas, associação de clientes e cálculo de totais. |

---

## 3. Fluxo de Navegação e Transição de Dados

### Navegação
- O arquivo `main.py` atua como o controlador central, permitindo ao usuário acessar os diferentes módulos do sistema (`tela_cliente`, `tela_produto` e `tela_venda`) através de menus ou botões de navegação principais.

### Transição de Dados
- Os dados inseridos nas interfaces são validados e persistidos utilizando as estruturas definidas em `models.py`, garantindo a comunicação correta entre a camada de visualização (as telas) e a camada de dados/regras de negócio.

---

## 4. Estrutura de Código e Arquitetura

###  Principais Arquivos e Módulos

- **`AppVendas/main.py`**: Inicializador principal da aplicação.
- **`AppVendas/models.py`**: Contém as classes, estruturas de dados e regras de persistência/entidades (como Clientes, Produtos e Vendas).
- **`AppVendas/tela_cliente.py`**: Módulo de interface voltado à gestão de clientes.
- **`AppVendas/tela_produto.py`**: Módulo de interface voltado à gestão de produtos e estoque.
- **`AppVendas/tela_venda.py`**: Módulo de interface voltado à realização e controle de vendas.

---

## 5. Regras de Negócio e Validações

O aplicativo implementa verificações essenciais para garantir a integridade operacional:
1. **Campos Obrigatórios:** Impedem o cadastro de registros com informações essenciais em branco (ex: nome do cliente, descrição do produto).
2. **Consistência de Estoque e Valores:** Validação de tipos de dados numéricos (preços, quantidades) para evitar erros de cálculo nas vendas.

---

## 6. Instruções para Execução

###  Requisitos Mínimos
- **Python:** Versão `3.13` ou superior.
- Ambiente operacional com suporte a execução de scripts Python e interface gráfica.

###  Passo a Passo para Executar Localmente

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/davimerlo21/appvendas.git](https://github.com/davimerlo21/appvendas.git)
