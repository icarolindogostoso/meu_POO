from cliente import Cliente, Clientes

class UI:
    def menu():
        print("1 - Inserir cliente, 2 - Listar clientes, 3 - Atualizar cliente, 9 - Fim")
        return int(input("Informe uma opção: "))

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

    @classmethod
    def inserir_cliente(cls):
        # id = int(input("Informe o id: "))
        nome = input("Infome o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        cliente = Cliente(0, nome, email, fone)
        Clientes.inserir(cliente)

    @classmethod
    def listar_clientes(cls):
        clientes = Clientes.listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(cliente)

    @classmethod
    def atualizar_clientes(cls):
        cls.listar_clientes()
        id = int(input("Informe o id do cliente a ser alterado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo email: ")
        fone = input("Informe o novo fone: ")
        cliente = Cliente(id, nome, email, fone)
        Clientes.atualizar(cliente)

UI.main()