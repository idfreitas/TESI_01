import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
lista = ['teste', 'TESTE']
lista_email = ['@samuel', 'Santos@']
lista_cpf = ['000000', '00000000', '00000000']
class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Treeview Tabela')
        self.janela.geometry('460x300')

        self.frm_botoes= tk.Frame(self.janela)
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['nome', 'cpf', 'email'] #cria as colunas com lista
        self.tvw = ttk.Treeview(self.janela, show='headings', columns=colunas)
        self.tvw.pack(side=tk.LEFT, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('cpf', text='Cpf')
        self.tvw.heading('email', text='Email')

        self.tvw.column('nome', minwidth=0, width=100)
        self.tvw.column('cpf', minwidth=0, width=150)
        self.tvw.column('email', minwidth=0, width=180)


        for a in range(len(lista)):
            self.tvw.insert('', 'end', values=(lista[a], lista_email[a], lista_cpf[a]))
        self.scr = ttk.Scrollbar(self.janela, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)

app = tk.Tk()
Tela(app)
app.mainloop()