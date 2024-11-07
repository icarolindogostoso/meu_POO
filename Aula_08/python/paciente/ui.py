from paciente import Paciente
from datetime import datetime

class UI:
    mauricio = None
    @classmethod
    def menu():
        print("1 - Criar paciente, 2 - Informar a idade do paciente, 9 - fim")
        return int(input("Informe a opção: "))
    
    @classmethod
    def main():
        op = 0
        while op != 9:
            if op == 1:
                UI.criar_paciente()
            if op == 2:
                UI.mostrar_idade()

    @classmethod
    def criar_paciente (cls):
        nome = input("Informe o nome: ")
        cpf = input("Informe o cpf: ")
        telefone = input("Informe o telefone: ")
        data = datetime.strftime(input("Informe a data"), %d%m%Y)
        cls.mauricio =
