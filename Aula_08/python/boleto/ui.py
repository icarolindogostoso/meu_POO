from datetime import datetime
from boleto import Boleto

class UI:
    boleto = None
    def menu():
        print("1 - Gerar boleto, 2 - Pagar boleto, 3 - Conferir situacao de pagamento, 9 - Fim")
        return int(input("Informe sua opção: "))
    
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.gerarBoleto()
            if op == 2:
                UI.pagarBoleto()
            if op == 3:
                UI.conferir()

    @classmethod
    def gerarBoleto(cls):
        cod = input("Informe o codigo de barras: ")
        emissao = datetime.today()
        vencimento = datetime.strptime(input("Informe uma data de vencimento: "), "%d/%m/%Y")
        valor = float(input("Informe o valor: "))
        cls.boleto = Boleto(cod,emissao,vencimento,valor)

    @classmethod
    def pagarBoleto (cls):
        valor = float(input("Informe o valor do pagamento: "))
        cls.boleto.pagar(valor)

    @classmethod
    def conferir (cls):
        print(cls.boleto)

UI.main()