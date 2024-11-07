from paciente import *
from datetime import datetime

class UI:
    mauricio = None
    def menu():
        print("1 - Criar paciente, 2 - Informar a idade do paciente, 3 - Mostrar paciente, 9 - fim")
        return int(input("Informe a opção: "))
    
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.criar_paciente()
            if op == 2:
                UI.mostrar_idade()
            if op == 3:
                UI.mostrar_paciente()

    @classmethod
    def criar_paciente (cls):
        nome = input("Informe o nome: ")
        cpf = input("Informe o cpf: ")
        telefone = input("Informe o telefone: ")
        data = datetime.strptime(input("Informe a data de nasciemento: "), "%d/%m/%Y")
        cls.mauricio = Paciente(nome,cpf,telefone,data)

    @classmethod
    def mostrar_idade (cls):
        if cls.mauricio == None:
            print("Paicente não criado")
        else:
            print(cls.mauricio.idade())

    @classmethod
    def mostrar_paciente(cls):
        print(cls.mauricio)

UI.main()