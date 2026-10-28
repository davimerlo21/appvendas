# tela_cliente.py
import tkinter as tk
from tkinter import messagebox
from models import Cliente, lista_clientes

class TelaCliente(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cadastro de Cliente")
        self.geometry("400x350")
        
        # Criação dos rótulos e campos de entrada
        tk.Label(self, text="Índice (ID):").pack(pady=2)
        self.entry_id = tk.Entry(self)
        self.entry_id.pack()

        tk.Label(self, text="Nome:").pack(pady=2)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack()

        tk.Label(self, text="CPF:").pack(pady=2)
        self.entry_cpf = tk.Entry(self)
        self.entry_cpf.pack()

        tk.Label(self, text="Telefone:").pack(pady=2)
        self.entry_telefone = tk.Entry(self)
        self.entry_telefone.pack()

        tk.Label(self, text="Apelido:").pack(pady=2)
        self.entry_apelido = tk.Entry(self)
        self.entry_apelido.pack()

        tk.Label(self, text="Turma/Turno:").pack(pady=2)
        self.entry_turma = tk.Entry(self)
        self.entry_turma.pack()

        # Botão para salvar
        tk.Button(self, text="Salvar Cliente", command=self.salvar_cliente, bg="green", fg="white").pack(pady=15)

    def salvar_cliente(self):
        # Coleta de dados da interface
        idx = self.entry_id.get()
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        tel = self.entry_telefone.get()
        apelido = self.entry_apelido.get()
        turma = self.entry_turma.get()

        # Validação básica
        if not idx or not nome:
            messagebox.showerror("Erro", "Índice e Nome são obrigatórios!")
            return

        # Cria a instância e adiciona à lista global
        novo_cliente = Cliente(idx, nome, cpf, tel, apelido, turma)
        lista_clientes.append(novo_cliente)
        
        messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")
        self.destroy() # Fecha a janela atual
