from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, saldo):
        super().__init__(numero_conta, cliente, saldo)