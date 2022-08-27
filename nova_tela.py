import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from cliente import Cliente
from contapoupanca import ContaPoupanca
from contacorrente import ContaCorrente
from banco import Banco
class Tela2:
    def __init__(self, master):
        self.pg_inicial = master
        self.pg_inicial.title('Página inicial')
        self.pg_inicial.geometry('900x400')
        self.clientes = []
        self.conta_pou = []
        self.conta_cor = []
        self.banco = []
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
        self.menu2.add_command(label='Contas poupança', command=self.poupanca)
        self.menu2.add_separator()
        self.menu2.add_command(label='Contas corrente', command=self.corrente)

        self.menu3.add_command(label="Cadastrar Banco", command=self.cadastro_banco)
        self.menu3.add_separator()
        self.menu3.add_command(label="Cadastrar Banco", command=self.bancos)

        self.pg_inicial.config(menu=self.barra)

    def cadastro_banco(self):
        self.tl_cadastro_banco = tk.Toplevel()
        self.tl_cadastro_banco.grab_set()
        self.tl_cadastro_banco.title('Cadastro do Banco')
        self.tl_cadastro_banco.geometry('800x600')

        self.frm_cadastro_banco = tk.Frame(self.tl_cadastro_banco)
        self.frm_cadastro_banco.place(relx=.5, rely=.5, anchor=tk.CENTER)

        # Titulo do fomulário
        self.lbl_titulo = tk.Label(self.frm_cadastro_banco, text='Cadastrar Banco', bg='blue', fg='white')
        self.lbl_titulo.grid(row=0, column=1, sticky=tk.W)

        # Nome do banco
        self.lbl_nome_banco = tk.Label(self.frm_cadastro_banco, text='Informe o nome do banco ')
        self.lbl_nome_banco.grid(row=1, column=0, sticky=tk.E)

        self.ent_nome_banco = tk.Entry(self.frm_cadastro_banco, width=35)
        self.ent_nome_banco.grid(row=1, column=1, ipady=5)

        # Número do Banco
        self.lbl_num_banco = tk.Label(self.frm_cadastro_banco, text='Informe o número do Banco')
        self.lbl_num_banco.grid(row=2, column=0, sticky=tk.E)

        self.ent_num_banco = tk.Entry(self.frm_cadastro_banco, width=35)
        self.ent_num_banco.grid(row=2, column=1, ipady=5)

        # Botão para salvar dados do cadastro
        self.btn_salvar_banco = tk.Button(self.frm_cadastro_banco, text='Salvar', bg='green', fg='white',
                                          command=self.salvar_cadastro_banco)
        self.btn_salvar_banco.grid(row=3, column=1, columnspan=2, sticky=tk.EW)
        ##################Verificações para cadastrar banco ########################

    def salvar_cadastro_banco(self):
        verifica = True
        if self.ent_nome_banco.get() == '' or self.ent_num_banco.get() == '':
            messagebox.showinfo('Aviso', 'Preencha todos os campos do cadastro!!', parent=self.tl_cadastro_banco)
            verifica = False

        if verifica == True:
            nome = self.ent_nome_banco.get()
            num = self.ent_num_banco.get()

            banco = Banco(nome, num)
            self.banco.append(banco)
            self.tl_cadastro_banco.destroy()
            self.pg_inicial.deiconify()
            messagebox.showinfo('Aviso', 'Cadastro realizado com sucesso!')

    def bancos(self):
        self.ls_banco = tk.Toplevel()
        self.ls_banco.grab_set()
        self.ls_banco.title('Lista dos Banco')
        self.ls_banco.geometry('600x300')

        self.frm_botoes = tk.Frame(self.ls_banco)
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['num_banco', 'nome']  # cria as colunas com lista
        self.tvw = ttk.Treeview(self.ls_banco, show='headings', columns=colunas)
        self.tvw.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('num_banco', text='Numero da conta')
        self.tvw.heading('nome', text='Cliente')


        self.tvw.column('num_banco', minwidth=0, width=100)
        self.tvw.column('nome', minwidth=0, width=150)


        self.tvw.insert('', 'end', values=('01', 'Banco Central'))
        for i in self.banco:
            self.tvw.insert('', 'end', values=(i.numero_bc, i.nome_bc))

        self.btn_atualizar = tk.Button(self.frm_botoes, text='Contas do Banco', bg='green', fg='white', command=self.tela_todas_contas)
        self.btn_atualizar.pack(side=tk.RIGHT)

        self.scr = ttk.Scrollbar(self.ls_banco, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)

    def tela_todas_contas(self):
        self.exibe_contas = tk.Toplevel()
        self.exibe_contas.grab_set()
        self.exibe_contas.title('Todas as contas')
        self.exibe_contas.geometry('1200x300')

        self.frm_botoes = tk.Frame(self.exibe_contas)
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['num_conta', 'cliente', 'saldo','tipo']  # cria as colunas com lista
        self.tvw = ttk.Treeview(self.exibe_contas, show='headings', columns=colunas)
        self.tvw.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.tvw1 = ttk.Treeview(self.exibe_contas, show='headings', columns=colunas)
        self.tvw1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # cabeçalho de tvw
        self.tvw.heading('num_conta', text='Nome da conta')
        self.tvw.heading('cliente', text='Dados do cliente')
        self.tvw.heading('saldo', text='Saldo')
        self.tvw.heading('tipo', text='Tipo')
        # colunas de tvw
        self.tvw.column('num_conta', minwidth=0, width=100)
        self.tvw.column('cliente', minwidth=0, width=200)
        self.tvw.column('saldo', minwidth=0, width=100)
        self.tvw.column('tipo', minwidth=0, width=180)

        self.tvw.insert('', 'end', values=('01', 'Maria 000.000.000-11', '1000', 'Poupança'))
        for p in self.conta_pou:
            self.tvw.insert('', 'end', values=(p.numero_conta, p.cliente, p.saldo, 'Poupança'))

        # cabeçalho de tvw1
        self.tvw1.heading('num_conta', text='Nome da conta')
        self.tvw1.heading('cliente', text='Dados do cliente')
        self.tvw1.heading('saldo', text='Saldo')
        self.tvw1.heading('tipo', text='Tipo')
        # colunas de tvw1
        self.tvw1.column('num_conta', minwidth=0, width=100)
        self.tvw1.column('cliente', minwidth=0, width=200)
        self.tvw1.column('saldo', minwidth=0, width=100)
        self.tvw1.column('tipo', minwidth=0, width=180)
        self.tvw1.insert('', 'end', values=('02', 'João 000.000.000-11', '1000', 'Corrente'))
        for c in self.conta_cor:
            self.tvw.insert('', 'end', values=(c.numero_conta, c.cliente, c.saldo, 'Corrente'))

        self.scr = ttk.Scrollbar(self.exibe_contas, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)



    ############ Tela de cadastro de novos clientes ##########################################3
    def cadastrar_cliente(self):
        self.tl_cadastro = tk.Toplevel()
        self.tl_cadastro.grab_set()
        self.tl_cadastro.title('Cadastro')
        self.tl_cadastro.geometry('800x400')

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
        self.btn_salvar = tk.Button(self.frm_cadastro, text='Salvar', bg='green', fg='white',
                                    command=self.salvar_cadastro)
        self.btn_salvar.grid(row=9, column=1, columnspan=2, sticky=tk.EW)
    ##################Virificações para salvar novo cliente ########################
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
        self.pg_clientes.geometry('600x300')

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

        self.btn_atualizar = tk.Button(self.frm_botoes, text='Atualizar dados do cliente', bg='green', fg='white', command=self.tela_atualizar)
        self.btn_atualizar.pack(side=tk.LEFT)
        self.btn_atualizar = tk.Button(self.frm_botoes, text='Remover cliente', bg='red', fg='white', command=self.remove_cliente)
        self.btn_atualizar.pack(side=tk.LEFT)

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
        for d in self.clientes:
            if d.cpf == c:
                d.nome = self.ent_nome.get()
                d.endereco = e
        if n != self.lista[0] or c != self.lista[1] or e != self.lista[2]:
            self.top_atualizar.destroy()
            self.pg_clientes.deiconify()

        else:
            messagebox.showinfo('Aviso', 'Realize alguma alteração para Atualizar!', parent=self.top_atualizar)

    def remove_cliente(self):
        var = messagebox.askquestion('Cuidado', 'Você está certo disso?')
        self.selecionado = self.tvw.selection()
        self.lista = self.tvw.item(self.selecionado, 'values')
        aux = True
        for x in self.conta_pou:
            if x.cliente[1] == self.lista[1]:
                aux = False
        for y in self.conta_cor:
            if y.cliente[1] == self.lista[1]:
                aux = False
        if aux == False:
            messagebox.showinfo('Aviso', 'Impossível Remover, pois cliente tem uma conta!')
        else:
            if var == 'yes':
                self.tvw.delete(self.selecionado)
                messagebox.showinfo('Aviso', 'Cliente removido!')

    ########## Tela que exibe os clientes e atraves dela permite selecionar cliente e criar conta #########
    def criar_conta(self):

        self.tl_contas = tk.Toplevel()
        self.tl_contas.grab_set()
        self.tl_contas.title('Criar contas')
        self.tl_contas.geometry('600x300')

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

        self.btn_atualizar = tk.Button(self.frm_botoes, text='Criar nova conta', bg='green', fg='white', command=self.cadastrar_conta)
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

            # pegando informações anteriores do treeview
            selecionado = self.tvw.selection()
            self.lista = self.tvw.item(selecionado, 'values')
            self.ent_nome_cliente.insert(1, self.lista[0])

        elif len(self.lista) == 0:
            messagebox.showinfo('Aviso', 'Selecione uma opção')
        else:  # Avisa ao Usuário a selecionar uma opção
            messagebox.showinfo('Aviso', 'Selecione apenas uma opção')
        self.btn_confirmar = tk.Button(self.cad_conta, bg='green', fg='white', text='Cadastrar',
                                       command=self.confirma_cadastro_conta)
        self.btn_confirmar.grid(row=5, column=1)

    def confirma_cadastro_conta(self):
        num_conta = self.ent_num_conta.get()
        saldo = float(self.ent_saldo.get())
        tipo_conta = self.cbx.get()
        if tipo_conta == 'Poupança':
            pou = ContaPoupanca(num_conta, self.lista, saldo)
            self.conta_pou.append(pou)

        else:
            cor = ContaCorrente(num_conta, self.lista, saldo)
            self.conta_cor.append(cor)
        if num_conta == '' or saldo == '':
            messagebox.showinfo('Aviso', 'Preencha todos os campos do cadastro!!', parent=self.cad_conta)


        else:
            self.cad_conta.destroy()
            self.tl_contas.deiconify()
            messagebox.showinfo('Aviso', 'Cadastro realizado com sucesso!')


    ####### Tela para exibir comtas ja criadas ###############
    def poupanca(self):
        self.contas_pou = tk.Toplevel()
        self.contas_pou.grab_set()
        self.contas_pou.title('Lista Poupança')
        self.contas_pou.geometry('600x300')

        self.frm_botoes = tk.Frame(self.contas_pou)
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['num_conta', 'cliente', 'saldo']  # cria as colunas com lista
        self.tvw = ttk.Treeview(self.contas_pou, show='headings', columns=colunas)
        self.tvw.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('num_conta', text='Numero da conta')
        self.tvw.heading('cliente', text='Cliente')
        self.tvw.heading('saldo', text='Saldo')

        self.tvw.column('num_conta', minwidth=0, width=100)
        self.tvw.column('cliente', minwidth=0, width=150)
        self.tvw.column('saldo', minwidth=0, width=180)

        self.tvw.insert('', 'end', values=('133', '000.000.000-01', '100'))
        for i in self.conta_pou:
            self.tvw.insert('', 'end', values=(i.numero_conta, i.cliente, i.saldo))

        self.btn_sacar_pou = tk.Button(self.frm_botoes, text='Sacar', bg='blue', fg='white', command=self.saque)
        self.btn_sacar_pou.pack(side=tk.LEFT)
        self.btn_deposita_pou = tk.Button(self.frm_botoes, text='Depositar', bg='green', fg='white',command=self.deposito)
        self.btn_deposita_pou.pack(side=tk.LEFT)
        self.btn_deposita_pou = tk.Button(self.frm_botoes, text='Atualizar', bg='orange', fg='white', command=self.atualizar_pou)
        self.btn_deposita_pou.pack(side=tk.LEFT)
        self.btn_encerrar_pou = tk.Button(self.frm_botoes, text='Encerrar conta', bg='red', fg='white', command=self.encerrar)
        self.btn_encerrar_pou.pack(side=tk.LEFT)
        self.scr = ttk.Scrollbar(self.contas_pou, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)

    def corrente(self):
        self.contas_cor = tk.Toplevel()
        self.contas_cor.grab_set()
        self.contas_cor.title('Lista das contas corrente')
        self.contas_cor.geometry('600x300')

        self.frm_botoes = tk.Frame(self.contas_cor)
        self.frm_botoes.pack(side=tk.BOTTOM)

        colunas = ['num_conta', 'cliente', 'saldo']  # cria as colunas com lista
        self.tvw = ttk.Treeview(self.contas_cor, show='headings', columns=colunas)
        self.tvw.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # cabeçalho
        self.tvw.heading('num_conta', text='Numero da conta')
        self.tvw.heading('cliente', text='Cliente')
        self.tvw.heading('saldo', text='Saldo')

        self.tvw.column('num_conta', minwidth=0, width=100)
        self.tvw.column('cliente', minwidth=0, width=150)
        self.tvw.column('saldo', minwidth=0, width=180)

        self.tvw.insert('', 'end', values=('012', '00000000000', '200'))
        for i in self.conta_cor:
            self.tvw.insert('', 'end', values=(i.numero_conta, i.cliente, i.saldo))

        self.btn_sacar_cor = tk.Button(self.frm_botoes, text='Sacar', bg='blue', fg='white', command=self.saque)
        self.btn_sacar_cor.pack(side=tk.LEFT)
        self.btn_deposita_cor = tk.Button(self.frm_botoes, text='Depositar', bg='green', fg='white', command=self.deposito)
        self.btn_deposita_cor.pack(side=tk.LEFT)
        self.btn_encerrar_cor = tk.Button(self.frm_botoes, text='Encerrar conta', bg='red', fg='white', command=self.encerrar)
        self.btn_encerrar_cor.pack(side=tk.LEFT)

        self.scr = ttk.Scrollbar(self.contas_cor, command=self.tvw.yview)
        self.scr.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=self.scr.set)

    def saque(self):
        self.lista = self.tvw.selection()

        if len(self.lista) == 1:
            self.tela_saque = tk.Toplevel()
            self.tela_saque.grab_set()
            self.tela_saque.title('Pagina de Saque')
            self.tela_saque.geometry('300x200')

            self.lbl_saldo_atual = tk.Label(self.tela_saque, text='Seu saldo atual é: ')
            self.lbl_saldo_atual.grid(row=0, column=0)
            self.lbl_valor = tk.Label(self.tela_saque, text='Informe o valor do saque:')
            self.lbl_valor.grid(row=1, column=0)

            self.ent_saldo_atual = tk.Entry(self.tela_saque, width=30)
            self.ent_saldo_atual.grid(row=0, column=1)

            self.ent_valor = tk.Entry(self.tela_saque, width=30)
            self.ent_valor.grid(row=1, column=1)

            # pegando informações anteriores do treeview
            selecionado = self.tvw.selection()
            self.lista = self.tvw.item(selecionado, 'values')
            self.ent_saldo_atual.insert(2, self.lista[2])
            self.btn_confirmar = tk.Button(self.tela_saque, text='Confirmar', command=self.confirma_saque)
            self.btn_confirmar.grid(row=3, column=1)
        elif len(self.lista) == 0:
            messagebox.showinfo('Aviso', 'Selecione uma opção')
        else:  # Avisa ao Usuário a selecionar uma opção
            messagebox.showinfo('Aviso', 'Selecione apenas uma opção')

    def confirma_saque(self):
        novo_saldo = float(self.ent_valor.get())
        aux = self.lista[0]

        for d in self.conta_pou:
            if d.numero_conta == aux:
                d.sacar(float(novo_saldo))
        for e in self.conta_cor:
            if e.numero_conta == aux:
                e.sacar(novo_saldo)
        self.tela_saque.destroy()

    def deposito(self):
        self.lista = self.tvw.selection()

        if len(self.lista) == 1:
            self.tela_deposito = tk.Toplevel()
            self.tela_deposito.grab_set()
            self.tela_deposito.title('Pagina de Saque')
            self.tela_deposito.geometry('300x200')

            self.lbl_saldo_atual = tk.Label(self.tela_deposito, text='Seu saldo atual é: ')
            self.lbl_saldo_atual.grid(row=0, column=0)
            self.lbl_valor = tk.Label(self.tela_deposito, text='Informe o valor do deposito:')
            self.lbl_valor.grid(row=1, column=0)

            self.ent_saldo_atual = tk.Entry(self.tela_deposito, width=30)
            self.ent_saldo_atual.grid(row=0, column=1)

            self.ent_valor = tk.Entry(self.tela_deposito, width=30)
            self.ent_valor.grid(row=1, column=1)

            # pegando informações anteriores do treeview
            selecionado = self.tvw.selection()
            self.lista = self.tvw.item(selecionado, 'values')
            self.ent_saldo_atual.insert(2, self.lista[2])
            self.btn_confirmar = tk.Button(self.tela_deposito, text='Confirmar', command=self.confirma_deposito)
            self.btn_confirmar.grid(row=3, column=1)
        elif len(self.lista) == 0:
            messagebox.showinfo('Aviso', 'Selecione uma opção')
        else:  # Avisa ao Usuário a selecionar uma opção
            messagebox.showinfo('Aviso', 'Selecione apenas uma opção')

    def confirma_deposito(self):
        novo_saldo = float(self.ent_valor.get())
        aux = self.lista[0]

        for d in self.conta_pou:
            if d.numero_conta == aux:
                d.deposito(float(novo_saldo))
        for e in self.conta_cor:
            if e.numero_conta == aux:
                e.deposito(novo_saldo)
        self.tela_deposito.destroy()

    def encerrar(self):
        var = messagebox.askquestion('Cuidado', 'Você está certo disso?')
        self.selecionado = self.tvw.selection()
        self.lista = self.tvw.item(self.selecionado, 'values')
        if float(self.lista[2]) != 0.0:
            messagebox.showinfo('Aviso', 'Impossível encerrar, pois saldo diferente de R$0.00!')
        else:
            if var == 'yes':
                self.tvw.delete(self.selecionado)
                messagebox.showinfo('Aviso', 'Conta encerrada!')


    def atualizar_pou(self):
        self.selecionado = self.tvw.selection()
        self.lista = self.tvw.item(self.selecionado, 'values')
        aux = self.lista[0]
        for a in self.conta_pou:
            if a.numero_conta == aux:
                a.atualizar()

app = tk.Tk()
Tela2(app)
app.mainloop()