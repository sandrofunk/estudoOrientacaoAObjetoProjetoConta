class Conta(object):

    def __init__(self, nome, senha, saldo):
        self.nome = nome
        self.senha = senha
        self.saldo = saldo

    def depositar(self, reais):
        self.saldo = self.saldo + reais

    def sacar(self, reais):
        if self.saldo < reais:
            print ('Saldo insuficiente')
        else:
            self.saldo = self.saldo - reais