# models.py

lista_clientes = []
lista_produtos = []
lista_vendas = []

class Cliente:
    def __init__(self, indice, nome, cpf, telefone, apelido, turma_turno):
        self.indice = indice
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.apelido = apelido
        self.turma_turno = turma_turno

class Produto:
    def __init__(self, indice, nome, unidade, valor):
        self.indice = indice
        self.nome = nome
        self.unidade = unidade
        self.valor = float(valor)

class Venda:
    def __init__(self, data, quantidade, vendedor, indice_cliente, indice_produto, valor_total):
        self.data = data
        self.quantidade = int(quantidade)
        self.vendedor = vendedor
        self.indice_cliente = indice_cliente
        self.indice_produto = indice_produto
        self.valor_total = valor_total
