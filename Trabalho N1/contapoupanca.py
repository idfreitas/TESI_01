from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, cliente, saldo):
        super().__init__(numero_conta, cliente, saldo)

    def atualizar(self, taxa):
        valor =  self.saldo * taxa * 3
        self.sacar(valor +0.9)
        return valor

    def encerrar_conta(self, valor):
        aux = valor
        if aux.saldo == 0:
            aux.remove(valor)
        else:
            print('Não foi possível excluir pois o slado NÃO É IGUAL A ZERO!')