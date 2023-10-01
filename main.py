from conta import Conta

minhaConta = Conta('Joãozinho', '123456', 1000.0)
print (minhaConta.saldo)

minhaConta.depositar(1000)
print(minhaConta.saldo)

minhaConta.sacar(500)
print(minhaConta.saldo)

minhaConta.sacar(3000)
print(minhaConta.saldo)