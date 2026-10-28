# main.py
import tkinter as tk
from tela_cliente import TelaCliente
from tela_produto import TelaProduto
from tela_venda import TelaVenda

class AppPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App Vendas/Compra")
        self.geometry("300x250")

        tk.Label(self, text="Menu Principal", font=("Arial", 16, "bold")).pack(pady=20)

        # Botões para abrir as respectivas telas separadas
        tk.Button(self, text="Cadastrar Cliente", width=20, command=self.abrir_cliente).pack(pady=5)
        tk.Button(self, text="Cadastrar Produto", width=20, command=self.abrir_produto).pack(pady=5)
        tk.Button(self, text="Registrar Venda", width=20, command=self.abrir_venda).pack(pady=5)

    def abrir_cliente(self):
        TelaCliente(self)

    def abrir_produto(self):
        TelaProduto(self)

    def abrir_venda(self):
        TelaVenda(self)

if __name__ == "__main__":
    app = AppPrincipal()
    app.mainloop()
