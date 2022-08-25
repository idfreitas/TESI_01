class Conta:
    def __init__(self, numero_conta, cliente, saldo):
        self._numemro_conta = numero_conta
        self._cliente = cliente
        self._saldo = saldo


    def deposito(self, valor):
       self._saldo += valor


    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print(f'Impossível realizar saque, pois seu saldo é de: {self._saldo}')


    def encerrar_conta(self, valor):
        aux = valor
        if aux.saldo == 0:
            aux.remove(valor)
        else:
            print('Não foi possível excluir pois o slado NÃO É IGUAL A ZERO!')

    # Acessando os atributos encapsulados da classe Conta
    @property
    def numero(self):
        return self._numemro_conta

    @numero.setter
    def numero(self, value):
        self._numemro_conta = value
    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo = value