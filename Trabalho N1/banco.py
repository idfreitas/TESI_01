
class Banco:
    def __init__(self, numero, nome):
        self._numero_bc = numero
        self._nome_bc = nome
        self._contas = []


    def recebe_contas(self, conta):
        self._contas.append(conta)

    def lista_contas_banco(self):
        for c in self._contas:
            print(f'Na conta {c.numero} tem por cliente {c.cliente.nome} que mora em {c.cliente.endereco} com um saldo igaul a: {c.saldo}')

    #Acessando os atributos encapsulados da classe banco
    @property
    def numero_bc(self):
        return self._numero_bc

    @numero_bc.setter
    def numero_bc(self, value):
        self._numero_bc = value

    @property
    def nome_bc(self):
        return self._nome_bc
    
    @nome_bc.setter
    def nome_bc(self, value):
        self._numero_bc = value

