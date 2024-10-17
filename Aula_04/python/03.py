class Conta_Bancaria:
    def __init__ (self):
        self.nome = ""
        self.n_conta = 0
        self.saldo = 0

    def m_saldo (self):
        print(f"Saldo atual: {self.saldo}")

    def deposito (self, valor):
        self.saldo = self.saldo + valor
        print("Deposito realizado com sucesso")

    def saque (self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - valor
            print("Saque realizado com sucesso")
            
cb = Conta_Bancaria()
cb.nome = input("Digite seu nome: ")
cb.n_conta = int(input("Digite o numero da sua conta: "))
cb.m_saldo()

valor = int(input("Digite quanto dinheiro voce quer depositar: "))
cb.deposito(valor)
cb.m_saldo()

valor = int(input("Digite quanto dinheiro voce quer sacar: "))
cb.saque(valor)