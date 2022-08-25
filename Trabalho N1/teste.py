from banco import Banco
from cliente import Cliente
from contapoupanca import ContaPoupanca
from contacorrente import ContaCorrente
b1 = Banco(12, 'Bradesco')
#def __init__(self, nome, endereco, cpf):
cli1 = Cliente('Samuel', 'Rio Branco', '000.111.222-33')
cli2 = Cliente('João', 'São Paulo', '111.222.333-44')

#conta Poupança (numero_conta, cliente, saldo)
print('===================================conta Poupança==============')
pou1 = ContaPoupanca(123, cli1, 0)
print(pou1.saldo)
print(f'A conta {pou1.numero} tem por cliente {pou1.cliente.nome} que mora em {pou1.cliente.endereco} com cpf {pou1.cliente.cpf} um saldo de: {pou1.saldo}')
pou1.deposito(0)
print(pou1.saldo)
print(pou1.numero)
#pou1.encerrar_conta(pou1)
#conta Corrente numero_conta, cliente, saldo
print('============================= COnta Corrente==========================')
cor1 = ContaCorrente(321, cli2, 1000)
print(f'A conta {cor1.numero} tem por cliente {cor1.cliente.nome} que mora em {cor1.cliente.endereco} com cpf {cor1.cliente.cpf} um saldo de: {cor1.saldo}')
print('=====================teste do banco =================================')
banco1 = Banco(13, 'Bradesco')
banco1.recebe_contas(pou1)
banco1.recebe_contas(cor1)
banco1.lista_contas_banco()