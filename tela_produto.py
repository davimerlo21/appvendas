# tela_produto.py
import tkinter as tk
from tkinter import messagebox
from models import Produto, lista_produtos

class TelaProduto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cadastro de Produto")
        self.geometry("400x300")

        tk.Label(self, text="Índice (ID):").pack(pady=2)
        self.entry_id = tk.Entry(self)
        self.entry_id.pack()

        tk.Label(self, text="Nome do Produto:").pack(pady=2)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack()

        tk.Label(self, text="Unidade (ex: Un, Kg, Litro):").pack(pady=2)
        self.entry_unidade = tk.Entry(self)
        self.entry_unidade.pack()

        tk.Label(self, text="Valor Unitário:").pack(pady=2)
        self.entry_valor = tk.Entry(self)
        self.entry_valor.pack()

        tk.Button(self, text="Salvar Produto", command=self.salvar_produto, bg="green", fg="white").pack(pady=15)

    def salvar_produto(self):
        idx = self.entry_id.get()
        nome = self.entry_nome.get()
        unidade = self.entry_unidade.get()
        valor = self.entry_valor.get()

        if not idx or not nome or not valor:
            messagebox.showerror("Erro", "Índice, Nome e Valor são obrigatórios!")
            return

        try:
            # Tenta converter o valor para salvar corretamente
            novo_produto = Produto(idx, nome, unidade, valor)
            lista_produtos.append(novo_produto)
            messagebox.showinfo("Sucesso", f"Produto {nome} cadastrado!")
            self.destroy()
        except ValueError:
            messagebox.showerror("Erro", "O campo Valor deve ser numérico.")
