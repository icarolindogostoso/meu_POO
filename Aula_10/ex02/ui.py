from os import ttyname
from view import View

class UI:
    @staticmethod
    def menu():
        print("1 - Inserir cliente, 2 - Listar clientes, 3 - Atualizar cliente, 9 - Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.inserir_cliente()
            if op == 2:
                UI.listar_clientes()
            if op == 3:
                UI.atualizar_clientes()

    @staticmethod
    def inserir_cliente():
        nome = input("Infome o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        View.inserir_cliente(nome, email, fone)

    @staticmethod
    def listar_clientes():
        clientes = View.clientes_listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(cliente)

    @staticmethod
    def atualizar_clientes():
        UI.listar_clientes()
        id = int(input("Informe o id do cliente a ser alterado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo email: ")
        fone = input("Informe o novo fone: ")
        View.atualizar_clientes(id, nome, email, fone)

    @staticmethod
    def excluir_clientes():
        UI.listar_clientes()
        id = int(input("Informe o id do cliente a ser excluido: "))
        View.excluir_clientes(id)

UI.main()