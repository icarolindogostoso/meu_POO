class ContaBancaria:
    def __init__ (self):
        self.__nome = ""
        self.__numeroConta = 0
        self.__saldo = 0

    def set_nome (self, v):
        if len(v) != 0:
            self.__nome = v
        else:
            raise ValueError ("Nome vazio")
        
    def set_numero_da_conta (self, v):
        if v > 1:
            self.__numeroConta = v
        else:
            raise ValueError ("Numero da conta nao pode ser um valor abaixo de um")
        
    def get_nome (self):
        return self.__nome
    
    def get_numero_da_conta (self):
        return self.__numeroConta
    
    def get_saldo (self):
        return self.__saldo
    
    def deposito (self, v):
        if v > 1:
            self.__saldo = self.__saldo + v
        else:
            raise ValueError ("Voce so pode depositar valores acima de 1")
        
    def saque (self, v):
        if v < self.__saldo:
            self.__saldo = self.__saldo - v
        else:
            raise ValueError ("Saldo insuficiente")
        
    
class UI:
    @staticmethod
    def main():
        x = ContaBancaria()

        x.set_nome(str(input("Informe seu nome: ")))
        x.set_numero_da_conta(int(input("Informe o numero da sua conta: ")))

        x.deposito(float(input("Informe qual o valor do depoisto: ")))
        x.saque(float(input("Informe o valor do saque: ")))

        print(f"Nome = {x.get_nome()}")
        print(f"Numero da conta = {x.get_numero_da_conta()}")
        print(f"Saldo = {x.get_saldo()}")

UI.main()