import tkinter as tk
from tkinter import Tk, messagebox
from tkinter import ttk
from cliente import Cliente
from contapoupanca import ContaPoupanca
from contacorrente import ContaCorrente
from banco import Banco
class Tela2:
    def __init__(self, master):
        self.pg_inicial = master
        self.pg_inicial.title('Página inicial')
        self.pg_inicial.geometry('1200x600')
        self.clientes = []
        self._conta_pou = []
        self._conta_cor = []
        ############ Página inicial com os menus ##################################################
        self.fr_menus_pag_inicial = tk.Frame(self.pg_inicial)
        self.fr_menus_pag_inicial.place(anchor=tk.NW)

        # parte do menu
        self.barra = tk.Menu(self.fr_menus_pag_inicial, fg='blue')
        self.menu1 = tk.Menu(self.barra, tearoff=0)
        self.menu2 = tk.Menu(self.barra, tearoff=0)
        self.menu3 = tk.Menu(self.barra, tearoff=0)

        self.barra.add_cascade(label='Cliente', menu=self.menu1)
        self.barra.add_cascade(label='Contas', menu=self.menu2)
        self.barra.add_cascade(label='Banco', menu=self.menu3)

        self.menu1.add_command(label='Cadastrar novo cliente', command=self.cadastrar_cliente)
        self.menu1.add_separator()
        self.menu1.add_command(label='Lista de clientes', command=self.lista_clientes)

        self.menu2.add_command(label='Criar contas', command=self.criar_conta)
        self.menu2.add_separator()
        self.menu2.add_command(label='lista de contas', command=self.lista_conta)

        self.menu3.add_command(label="Cadastrar Banco",command=self.cadastro_banco)
        self.menu3.add_separator()
        """
        self.menu3.add_command(label='Mostrar Banco', command=self.mostrar_banco)
        self.menu3.add_separator()
        self.menu3.add_command(label='Mostrar Banco', command=self.atualizar_banco)
        """
       

        self.pg_inicial.config(menu=self.barra)
    #########Banco####################
    def cadastro_banco(self):
        self.tl.cadastro_banco = tk.Toplevel()
        self.tl.cadastro_banco.grab_set()
        self.tl.cadastro_banco.title('Cadastro do Banco')
        self.tl.cadastro_banco.geometry('800x600')

        self.frm_cadastro_banco = tk.Frame(self.tl_cadastro)
        self.frm_cadastro_banco.place(relx=.5, rely=.5, anchor=tk.CENTER)

         # Titulo do fomulário
        self.lbl_titulo = tk.Label(self.frm_cadastro_banco, text='Cadastro do Banco', bg='blue', fg='white')
        self.lbl_titulo.grid(row=0, column=1, sticky=tk.W)

        # Primeiro nome do cadastrado
        self.lbl_nome = tk.Label(self.frm_cadastro_banco, text='Informe o nome do banco ')
        self.lbl_nome.grid(row=1, column=0, sticky=tk.E)

        self.ent_nome = tk.Entry(self.frm_cadastro_banco, width=35)
        self.ent_nome.grid(row=1, column=1, ipady=5)

        # Primeiro sobrenome do cadastrado
        self.lbl_cpf = tk.Label(self.frm_cadastro_banco, text='Informe o número do Banco')
        self.lbl_cpf.grid(row=2, column=0, sticky=tk.E)




    ############ Tela de cadastro de novos clientes ##########################################3
    

    def cadastrar_cliente(self):
        self.tl_cadastro = tk.Toplevel()
        self.tl_cadastro.grab_set()
        self.tl_cadastro.title('Cadastro')
        self.tl_cadastro.geometry('1200x600')

        self.frm_cadastro = tk.Frame(self.tl_cadastro)
        self.frm_cadastro.place(relx=.5, rely=.5, anchor=tk.CENTER)

        # Titulo do fomulário
        self.lbl_titulo = tk.Label(self.frm_cadastro, text='Cadastro de novos Usuários!', bg='blue', fg='white')
        self.lbl_titulo.grid(row=0, column=1, sticky=tk.W)

        # Primeiro nome do cadastrado
        self.lbl_nome = tk.Label(self.frm_cadastro, text='Informe seu nome completo: ')
        self.lbl_nome.grid(row=1, column=0, sticky=tk.E)

        self.ent_nome = tk.Entry(self.frm_cadastro, width=35)
        self.ent_nome.grid(row=1, column=1, ipady=5)

        # Primeiro sobrenome do cadastrado
        self.lbl_cpf = tk.Label(self.frm_cadastro, text='Informe seu cpf: ')
        self.lbl_cpf.grid(row=2, column=0, sticky=tk.E)

        self.ent_cpf = tk.Entry(self.frm_cadastro, width=35)
        self.ent_cpf.grid(row=2, column=1, ipady=5)


        # Parte endereço
        self.lbl_endereco = tk.Label(self.frm_cadastro, text='Informe seu endereço: ')
        self.lbl_endereco.grid(row=3, column=0, sticky=tk.E)

        self.ent_endereco = tk.Entry(self.frm_cadastro, width=35)
        self.ent_endereco.grid(row=3, column=1, ipady=5)

        # estado civil do cadastrado
        self.lbl_estado_cv = tk.Label(self.frm_cadastro, text='Seu estado civil: ')
        self.lbl_estado_cv.grid(row=4, column=0, sticky=tk.E)

        self.civil = tk.StringVar(self.frm_cadastro, '1')

        self.rbt_masculino = tk.Radiobutton(self.frm_cadastro, text='Solteiro', value='1', variable=self.civil)
        self.rbt_masculino.grid(row=4, column=1, sticky=tk.W)

        self.rbt_femenino = tk.Radiobutton(self.frm_cadastro, text='Casado', value='2', variable=self.civil)
        self.rbt_femenino.grid(row=5, column=1, sticky=tk.W)

        self.rbt_N = tk.Radiobutton(self.frm_cadastro, text='Outros', value='3', variable=self.civil)
        self.rbt_N.grid(row=6, column=1, sticky=tk.W)

        # Senha
        # Parte Matricula
        self.lbl_senha_cadast = tk.Label(self.frm_cadastro, text='Senha: ')
        self.lbl_senha_cadast.grid(row=7, column=0, sticky=tk.E)

        self.ent_senha_cadast = tk.Entry(self.frm_cadastro, width=35)
        self.ent_senha_cadast.grid(row=7, column=1, ipady=5)

        # Confirmação da senha
        self.lbl_confirma = tk.Label(self.frm_cadastro, text='Confirma senha: ')
        self.lbl_confirma.grid(row=8, column=0, sticky=tk.E)

        self.ent_confirma = tk.Entry(self.frm_cadastro, width=35)
        self.ent_confirma.grid(row=8, column=1, ipady=5)

        # Botão para salvar dados do cadastro
        self.btn_salvar = tk.Button(self.frm_cadastro, text='Salvar', bg='green', fg='white', command=self.salvar_cadastro)
        self.btn_salvar.grid(row=9, column=1, columnspan=2, sticky=tk.EW)
    ##################Verificações para salvar novo cliente ########################
    def salvar_cadastro(self):
        verifica = True
        if self.ent_nome.get() == '' or self.ent_cpf.get() == '' or self.ent_endereco.get() == '' or self.ent_senha_cadast.get() == '' or self.ent_confirma.get() == '':
            messagebox.showinfo('Aviso', 'Preencha todos os campos do cadastro!!', parent=self.tl_cadastro)
            verifica = False

        if self.ent_senha_cadast.get() != self.ent_confirma.get():
            messagebox.showinfo('Aviso', 'Confirmação de senha inválida!', parent=self.tl_cadastro)
            verifica = False

        if verifica == True:
            nome = self.ent_nome.get()
            cpf = self.ent_cpf.get()
            endereco = self.ent_endereco.get()
            cliente = Cliente(nome, cpf, endereco)
            self.clientes.append(cliente)
            self.tl_cadastro.destroy()
            self.pg_inicial.deiconify()
            messagebox.showinfo('Aviso', 'Cadastro realizado com sucesso!')



    #################### Tela da lista de clientes ##############################
    def lista_clientes(self):
        self.pg_clientes = tk.Toplevel()
        self.pg_clientes.grab_set()
        self.pg_clientes.title('Página dos Clientes')
        self.pg_clientes.geometry('1200x300')

        self.frm_botoes = tk.Frame(self.pg_clientes)
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['nome', 'cpf', 'endereco']  # cria as colunas com lista
        self.tvw = ttk.Treeview(self.pg_clientes, show='headings', columns=colunas)
        self.tvw.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('nome', text='Nome do cliente')
        self.tvw.heading('cpf', text='Cpf')
        self.tvw.heading('endereco', text='Endereço')

        self.tvw.column('nome', minwidth=0, width=100)
        self.tvw.column('cpf', minwidth=0, width=150)
        self.tvw.column('endereco', minwidth=0, width=180)

        self.tvw.insert('', 'end', values=('Samuel', '00000000000', 'Rio Branco'))
        self.tvw.insert('', 'end', values=('Marcelo', '00000000000', 'Sena Madureira'))
        self.tvw.insert('', 'end', values=('Maria', '00000000000', 'Brasileia'))
        self.tvw.insert('', 'end', values=('José', '00000000000', 'Xapuri'))
        self.tvw.insert('', 'end', values=('Felipe', '00000000000', 'São Paulo'))
        self.tvw.insert('', 'end', values=('joão', '00000000000', 'Minas Gerais'))
        for i in self.clientes:
            self.tvw.insert('', 'end', values=(i.nome, i.cpf, i.endereco))

        self.btn_atualizar = tk.Button(self.frm_botoes, text='Atualizar dados do cliente', command=self.tela_atualizar)
        self.btn_atualizar.pack(side=tk.RIGHT)

        self.scr = ttk.Scrollbar(self.pg_clientes, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)
    ####################### Tela de atualização da (Lista de Clientes) ##################3
    def tela_atualizar(self):
        # pegando informações do Treenview
        self.lista = self.tvw.selection()

        if len(self.lista) == 1:
            self.top_atualizar = tk.Toplevel()
            self.top_atualizar.grab_set()
            self.top_atualizar.title('Atualizar')
            self.top_atualizar.geometry('300x200')

            self.lbl_nome = tk.Label(self.top_atualizar, text='Nome: ')
            self.lbl_nome.grid(row=0, column=0)
            self.lbl_cpf = tk.Label(self.top_atualizar, text='Cpf: ')
            self.lbl_cpf.grid(row=1, column=0)
            self.lbl_endereco = tk.Label(self.top_atualizar, text='Endereço: ')
            self.lbl_endereco.grid(row=2, column=0)


            self.ent_nome = tk.Entry(self.top_atualizar, width=30)
            self.ent_nome.grid(row=0, column=1)

            self.ent_cpf = tk.Entry(self.top_atualizar, width=30)
            self.ent_cpf.grid(row=1, column=1)

            self.ent_endereco = tk.Entry(self.top_atualizar, width=30)
            self.ent_endereco.grid(row=2, column=1)

            # pegando informações anteriores do treeview
            selecionado = self.tvw.selection()
            self.lista = self.tvw.item(selecionado, 'values')
            self.ent_nome.insert(0, self.lista[0])
            self.ent_cpf.insert(1, self.lista[1])
            self.ent_endereco.insert(2, self.lista[2])
            self.btn_confirmar = tk.Button(self.top_atualizar, text='Confirmar', command=self.confirmar_atualiza)
            self.btn_confirmar.grid(row=3, column=1)
        elif len(self.lista) == 0:
            messagebox.showinfo('Aviso', 'Selecione uma opção')
        else:     # Avisa ao Usuário a selecionar uma opção
            messagebox.showinfo('Aviso', 'Selecione apenas uma opção')

    ############# Verifica os dados para realizar a atualização ######################
    def confirmar_atualiza(self):
        n = self.ent_nome.get()
        c = self.ent_cpf.get()
        e = self.ent_endereco.get()
        selecionado = self.tvw.selection()
        self.tvw.item(selecionado, values=(n, c, e))
        if n != self.lista[0] or c != self.lista[1] or e != self.lista[2]:
            self.top_atualizar.destroy()
            self.pg_clientes.deiconify()

        else:
            messagebox.showinfo('Aviso', 'Realize alguma alteração para Atualizar!', parent=self.top_atualizar)

    ########## Tela que exibe os clientes e atraves dela permite selecionar cliente e criar conta #########
    def criar_conta(self):

        self.tl_contas = tk.Toplevel()
        self.tl_contas.grab_set()
        self.tl_contas.title('Criar contas')
        self.tl_contas.geometry('1200x550')

        self.frm_botoes = tk.Frame(self.tl_contas)
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['nome', 'cpf', 'endereco']  # cria as colunas com lista
        self.tvw = ttk.Treeview(self.tl_contas, show='headings', columns=colunas)
        self.tvw.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('nome', text='Nome do cliente')
        self.tvw.heading('cpf', text='Cpf')
        self.tvw.heading('endereco', text='Endereço')

        self.tvw.column('nome', minwidth=0, width=100)
        self.tvw.column('cpf', minwidth=0, width=150)
        self.tvw.column('endereco', minwidth=0, width=180)

        self.tvw.insert('', 'end', values=('Samuel', '00000000000', 'Rio Branco'))
        self.tvw.insert('', 'end', values=('Marcelo', '00000000000', 'Sena Madureira'))
        self.tvw.insert('', 'end', values=('Maria', '00000000000', 'Brasileia'))
        for c in self.clientes:
            self.tvw.insert('', 'end', values=(c.nome, c.cpf, c.endereco))

        self.btn_atualizar = tk.Button(self.frm_botoes, text='Criar nova conta', command=self.cadastrar_conta)
        self.btn_atualizar.pack(side=tk.RIGHT)

        self.scr = ttk.Scrollbar(self.tl_contas, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)

    ################ Onde sera inserido os dados para a criação da conta #######
    def cadastrar_conta(self):

        # pegando informações do Treenview
        self.lista = self.tvw.selection()

        if len(self.lista) == 1:
            self.cad_conta = tk.Toplevel()
            self.cad_conta.grab_set()
            self.cad_conta.title('Atualizar')
            self.cad_conta.geometry('600x300')

            self.lbl_num_conta = tk.Label(self.cad_conta, text='Informe o numero da conta: ')
            self.lbl_num_conta.grid(row=0, column=0)
            self.lbl_nome_cliente = tk.Label(self.cad_conta, text='nome do cliente: ')
            self.lbl_nome_cliente.grid(row=1, column=0)
            self.lbl_saldo = tk.Label(self.cad_conta, text='saldo: ')
            self.lbl_saldo.grid(row=2, column=0)

            self.ent_num_conta = tk.Entry(self.cad_conta, width=30)
            self.ent_num_conta.grid(row=0, column=1)

            self.ent_nome_cliente = tk.Entry(self.cad_conta, width=30)
            self.ent_nome_cliente.grid(row=1, column=1)

            self.ent_saldo = tk.Entry(self.cad_conta, width=30)
            self.ent_saldo.grid(row=2, column=1)

            self.lbl_tipo_conta = tk.Label(self.cad_conta, text='Tipo de conta: ')
            self.lbl_tipo_conta.grid(row=3, column=0, sticky=tk.E)
            v = tk.StringVar()
            valor = v.get()
            self.cbx = ttk.Combobox(self.cad_conta, textvariable=valor)
            self.cbx.grid(row=4, column=1, sticky=tk.W)
            self.cbx['values'] = ('Poupança', 'Corrente')
            self.cbx.current(0)
            num = self.ent_num_conta.get()
            cli = Cliente
            sal = self.ent_saldo.get()
            if self.cbx.get() == 'Poupança':
                pou = ContaPoupanca(num, cli, sal)
                self._conta_pou.append(pou)
            else:
                cor = ContaCorrente(num, cli, sal)
                self._conta_cor.append(cor)
                print(self._conta_cor)

            # pegando informações anteriores do treeview
            selecionado = self.tvw.selection()
            self.lista = self.tvw.item(selecionado, 'values')
            self.ent_nome_cliente.insert(1, self.lista[0])

            self.btn_voltar = tk.Button(self.cad_conta, text='Voltar', bg='blue', fg='white', command=self.criar_conta)
            self.btn_voltar.grid(row=5, column=0, sticky=tk.E)

            self.btn_confirmar = tk.Button(self.cad_conta, bg='green', fg='white', text='Cadastrar')
            self.btn_confirmar.grid(row=5, column=1)

        elif len(self.lista) == 0:
            messagebox.showinfo('Aviso', 'Selecione uma opção')
        else:  # Avisa ao Usuário a selecionar uma opção
            messagebox.showinfo('Aviso', 'Selecione apenas uma opção')


    ####### Tela para exibir comtas ja criadas ###############
    def lista_conta(self):
        self.list_conta = tk.Toplevel()
        self.list_conta.grab_set()
        self.list_conta.title('Lista de clientes')
        self.list_conta.geometry('1200x300')

        self.frm_botoes = tk.Frame(self.list_conta)
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['nome', 'cpf', 'endereco']  # cria as colunas com lista
        self.tvw = ttk.Treeview(self.list_conta, show='headings', columns=colunas)
        self.tvw.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('nome', text='Nome do cliente')
        self.tvw.heading('cpf', text='Cpf')
        self.tvw.heading('endereco', text='Endereço')

        self.tvw.column('nome', minwidth=0, width=100)
        self.tvw.column('cpf', minwidth=0, width=150)
        self.tvw.column('endereco', minwidth=0, width=180)

        self.tvw.insert('', 'end', values=('Samuel', '00000000000', 'Rio Branco'))
        self.tvw.insert('', 'end', values=('Marcelo', '00000000000', 'Sena Madureira'))
        self.tvw.insert('', 'end', values=('Maria', '00000000000', 'Brasileia'))
        self.tvw.insert('', 'end', values=('José', '00000000000', 'Xapuri'))
        self.tvw.insert('', 'end', values=('Felipe', '00000000000', 'São Paulo'))
        self.tvw.insert('', 'end', values=('joão', '00000000000', 'Minas Gerais'))
        for i in self.clientes:
            self.tvw.insert('', 'end', values=(i.nome, i.cpf, i.endereco))

        self.btn_atualizar = tk.Button(self.frm_botoes, text='Atualizar dados do cliente', command=self.tela_atualizar)
        self.btn_atualizar.pack(side=tk.RIGHT)

        self.scr = ttk.Scrollbar(self.list_conta, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)

app = tk.Tk()
Tela2(app)
app.mainloop()