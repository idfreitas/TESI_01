import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tela2 import Tela2

class Login:
    def __init__(self, master):
        self.janela = master
        self.janela.geometry("1200x800")
        self.janela.title('Tela de login')

        self.frm_login = tk.Frame(self.janela)
        self.frm_login.place(relx=.5, rely=.5, anchor=tk.CENTER)

        self.lbl_login = tk.Label(self.frm_login, text='Login:')
        self.lbl_login.grid(row=0, column=0)

        self.ent_login = tk.Entry(self.frm_login, width='35')
        self.ent_login.grid(row=0, column=1, ipady=5)

        self.lbl_senha = tk.Label(self.frm_login, text='Senha:')
        self.lbl_senha.grid(row=1, column=0)

        self.ent_senha = tk.Entry(self.frm_login, width='35', show='*')
        self.ent_senha.grid(row=1, column=1, ipady=5)



        self.btn_entrar = tk.Button(self.frm_login, text='Entrar', bg='green', fg='white', command=self.logado)
        self.btn_entrar.grid(row=2, column=1, columnspan=2, sticky=tk.EW)

    def logado(self):
        if self.ent_login.get() == '' or self.ent_senha.get() == '':
            messagebox.showinfo('Aviso', 'Se você já é cadastrado preencha todos os campos do Login!',
                                    parent=self.janela)

        else:
            pass



app1 = tk.Tk()
Login(app1)
app1.mainloop()