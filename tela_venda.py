# tela_venda.py
import tkinter as tk
from tkinter import messagebox
from models import Venda, lista_clientes, lista_produtos, lista_vendas

class TelaVenda(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registrar Venda")
        self.geometry("400x400")

        tk.Label(self, text="Data da Venda:").pack(pady=2)
        self.entry_data = tk.Entry(self)
        self.entry_data.pack()

        tk.Label(self, text="Quantidade:").pack(pady=2)
        self.entry_quant = tk.Entry(self)
        self.entry_quant.pack()

        tk.Label(self, text="Vendedor:").pack(pady=2)
        self.entry_vendedor = tk.Entry(self)
        self.entry_vendedor.pack()

        tk.Label(self, text="Índice do Cliente:").pack(pady=2)
        self.entry_idx_cliente = tk.Entry(self)
        self.entry_idx_cliente.pack()

        tk.Label(self, text="Índice do Produto:").pack(pady=2)
        self.entry_idx_produto = tk.Entry(self)
        self.entry_idx_produto.pack()

        # Botão para calcular e finalizar a operação
        tk.Button(self, text="Finalizar Venda", command=self.efetuar_venda, bg="blue", fg="white").pack(pady=20)

    def efetuar_venda(self):
        data = self.entry_data.get()
        quant = self.entry_quant.get()
        vendedor = self.entry_vendedor.get()
        idx_cliente = self.entry_idx_cliente.get()
        idx_produto = self.entry_idx_produto.get()

        # Lógica Básica de Busca e Validação por Índice
        cliente_encontrado = next((c for c in lista_clientes if c.indice == idx_cliente), None)
        produto_encontrado = next((p for p in lista_produtos if p.indice == idx_produto), None)

        if not cliente_encontrado:
            messagebox.showerror("Erro", "Cliente não encontrado com o índice informado!")
            return
        
        if not produto_encontrado:
            messagebox.showerror("Erro", "Produto não encontrado com o índice informado!")
            return

        try:
            qnt = int(quant)
            # Cálculo automático do Valor Total (Lógica de negócio)
            valor_total = qnt * produto_encontrado.valor

            # Registra a venda
            nova_venda = Venda(data, qnt, vendedor, idx_cliente, idx_produto, valor_total)
            lista_vendas.append(nova_venda)

            # Exibe o resumo da operação concluída
            resumo = (f"Venda Realizada!\n\n"
                      f"Cliente: {cliente_encontrado.nome}\n"
                      f"Produto: {produto_encontrado.nome}\n"
                      f"Total: R$ {valor_total:.2f}")
            messagebox.showinfo("Sucesso", resumo)
            self.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida.")
