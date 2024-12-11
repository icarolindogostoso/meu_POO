from os import stat
from models.clientes import Cliente, Clientes
from models.categorias import Categoria, Categorias
from models.produtos import Produto, Produtos

class View:
    @staticmethod
    def clienteListar():
        return Clientes.listar()
    
    @staticmethod
    def clienteInserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        Clientes.inserir(c)

    @staticmethod
    def clienteAtualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)
    
    @staticmethod
    def clienteExcluir(id):
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)

    @staticmethod
    def categoriaListar():
        return Categorias.listar()

    @staticmethod
    def categoriaListarId(id):
        return Categorias.listar_id(id)
    
    @staticmethod
    def categoriaInserir(descricao):
        c = Categoria(0, descricao)
        Categorias.inserir(c)

    @staticmethod
    def categoriaAtualizar(id, descricao):
        c = Categoria(id, descricao)
        Categorias.atualizar(c)
    
    @staticmethod
    def categoriaExcluir(id):
        c = Categoria(id, "")
        Categorias.excluir(c)

    @staticmethod
    def produtoListar():
        return Produtos.listar()
    
    @staticmethod
    def produtoInserir(descricao, preco, estoque, id_categoria):
        c = Produto(0, descricao, preco, estoque, id_categoria)
        Produtos.inserir(c)

    @staticmethod
    def produtoAtualizar(id, descricao, preco, estoque, id_categoria):
        c = Produto(id, descricao, preco, estoque, id_categoria)
        Produtos.atualizar(c)
    
    @staticmethod
    def produtoExcluir(id):
        c = Produto(id, "", 0, 0, None)
        Produtos.excluir(c)

    @staticmethod
    def produtoReajustar(percentual):
        for obj in View.produtoListar():
            View.produtoAtualizar(obj.id, obj.descricao, obj.preco * (1 + percentual), obj.estoque, obj.id_categoria)