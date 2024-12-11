from os import ttyname
from view import View

class UI:
    @staticmethod
    def menu():
        print("\nCadastro de Clientes")
        print(" 1 - Inserir cliente, 2 - Listar clientes, 3 - Atualizar cliente, 4 - Excluir")
        print("\nCadastro de Categorias")
        print( "5 - Inserir, 6 - Listar, 7 - Atualizar, 8 - Exlcuir")
        print("\nCadastro de Produtos")
        print(" 9 - Inserir, 10 - Listar, 11 - Atualizar, 12 - Excluir, 13 - Reajustar")
        print(" 99 - Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 99:
            op = UI.menu()
            if op == 1:
                UI.clienteInserir()
            if op == 2:
                UI.clienteListar()
            if op == 3:
                UI.clienteAtualizar()
            if op == 4:
                UI.clienteExcluir()

            if op == 5:
                UI.categoriaInserir()
            if op == 6:
                UI.categoriaListar()
            if op == 7:
                UI.categoriaAtualizar()
            if op == 8:
                UI.categoriaExcluir()

            if op == 9:
                UI.produtoInserir()
            if op == 10:
                UI.produtoListar()
            if op == 11:
                UI.produtoAtualizar()
            if op == 12:
                UI.produtoExcluir()
            if op == 13:
                UI.produtoReajustar()

    @staticmethod
    def clienteInserir():
        nome = input("Infome o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        View.clienteInserir(nome, email, fone)

    @staticmethod
    def clienteListar():
        clientes = View.clienteListar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(cliente)

    @staticmethod
    def clienteAtualizar():
        UI.clienteListar()
        id = int(input("Informe o id do cliente a ser alterado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo email: ")
        fone = input("Informe o novo fone: ")
        View.clienteAtualizar(id, nome, email, fone)

    @staticmethod
    def clienteExcluir():
        UI.clienteListar()
        id = int(input("Informe o id do cliente a ser excluido: "))
        View.clienteExcluir(id)



    @staticmethod
    def categoriaInserir():
        descricao = input("Infome a descricao: ")
        View.categoriaInserir(descricao)

    @staticmethod
    def categoriaListar():
        categorias = View.categoriaListar()
        if len(categorias) == 0:
            print("Nenhuma categoria cadastrada")
        else:
            for categoria in categorias:
                print(categoria)

    @staticmethod
    def categoriaAtualizar():
        UI.categoriaListar()
        id = int(input("Informe o id da categoria a ser alterada: "))
        descricao = input("Informe a nova descricao: ")
        View.categoriaAtualizar(id, descricao)

    @staticmethod
    def categoriaExcluir():
        UI.categoriaListar()
        id = int(input("Informe o id da categoria a ser excluida: "))
        View.categoriaExcluir(id)



    @staticmethod
    def produtoInserir():
        descricao = input("Infome a descricao: ")
        estoque = int(input("Informe o estoque: "))
        preco = float(input("Informe o preco: "))
        UI.categoriaListar()
        id_categoria = int(input("Informe o id da categoria: "))
        View.produtoInserir(descricao, preco, estoque, id_categoria)

    @staticmethod
    def produtoListar():
        produtos = View.produtoListar()
        if len(produtos) == 0:
            print("Nenhum produto cadastrado")
        else:
            for produto in produtos:
                id_categoria = produto.id_categoria
                categoria = View.categoriaListarId(id_categoria)
                print(f"{produto} + '-' + {categoria.descricao}")

    @staticmethod
    def produtoAtualizar():
        UI.produtoListar()
        id = int(input("Informe o id do produto a ser alterado: "))
        descricao = input("Informe a nova descricao: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe o novo estoque: "))
        UI.categoriaListar()
        id_categoria = int(input("Informe o id da categoria"))
        View.categoriaAtualizar(id, descricao, preco, estoque, id_categoria)

    @staticmethod
    def produtoExcluir():
        UI.produtoListar()
        id = int(input("Informe o id do produto a ser excluido: "))
        View.categoriaExcluir(id)

    @staticmethod
    def produtoReajustar():
        reajuste = float(input("Informe o percentual de reajuste em %: "))
        View.produtoReajustar(reajuste / 100)

UI.main()