from view import View

class UI:
    @staticmethod
    def menu():
        print("1 - Listar Produto, 2 - Inserir Produto, 3 - Atualizar Produto, 4 - Excluir Produto, 5 - Listar Categoria, 6 - Inserir Categoria, 7 - Atualizar Categoria, 8 - Excluir Categoria, 9 - Listar Cliente, 10 - Inserir Cliente, 11 - Atualizar Cliente, 12 - Excluir Cliente, 13 - Fim")
        return int(input("Informe a sua opção: "))
    
    @staticmethod
    def main():
        op = 0
        while op != 13:
            op = UI.menu()
            if op == 1:
                UI.produtoListar()
            if op == 2:
                UI.produtoInserir()
            if op == 3:
                UI.produtoAtualizar()
            if op == 4:
                UI.produtoExcluir()
            if op == 5:
                UI.categoriaListar()
            if op == 6:
                UI.categoriaInserir()
            if op == 7:
                UI.categoriaAtualizar()
            if op == 8:
                UI.categoriaExcluir()
            if op == 9:
                UI.clienteListar()
            if op == 10:
                UI.clienteInserir()
            if op == 11:
                UI.clienteAtualizar()
            if op == 12:
                UI.clienteExcluir()
            
    @staticmethod
    def produtoListar ():
        produtos = View.produtoListar()
        if len(produtos) == 0:
            print("Nenhum produto cadastrado")
        else:
            for produto in produtos:
                print(produto)

    @staticmethod
    def produtoInserir():
        descricao = input("Informe a descricao do produto: ")
        preco = float(input("Informe o preco do produto: "))
        estoque = int(input("Informe quantos produtos tem no estoque: "))
        View.produtoInserir(descricao, preco, estoque)

    @staticmethod
    def produtoAtualizar():
        UI.produtoListar()
        id = int(input("Informe o id do produto a ser alterado: "))
        descricao = input("Informe a nova descricao: ")
        preco = float(input("Informe o novo preco: "))
        estoque = int(input("Informe o novo estoque: "))
        View.produtoAtualizar(id, descricao, preco, estoque)

    @staticmethod
    def produtoExcluir():
        UI.produtoListar()
        id = int(input("Informe o id do produto a ser excluido: "))
        View.produtoExcluir(id)

    @staticmethod
    def categoriaListar():
        categorias = View.categoriaListar()
        if len(categorias) == 0:
            print("Nenhuma categoria cadastrada")
        else:
            for categoria in categorias:
                print(categoria)

    @staticmethod
    def categoriaInserir():
        descricao = input("Informe a descricao da categoria: ")
        View.categoriaInserir(descricao)

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
    def clienteListar():
        clientes = View.clienteListar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(cliente)

    @staticmethod
    def clienteInserir():
        nome = input("Infome o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        View.clienteInserir(nome, email, fone)

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