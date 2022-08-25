class Cliente:

    def __init__(self, nome, cpf, endereco):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco

    # Acessando os atributos encapsulados da classe Cliente
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, value):
        self._endereco = value