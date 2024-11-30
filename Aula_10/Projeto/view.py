from models.clientes import Cliente, Clientes
from models.categorias import Categoria, Categorias
from models.produtos import Produto, Produtos

class View:
    @staticmethod
    def produtoListar():
        return Produtos.listar()
    
    @staticmethod
    def produtoInserir(descricao, preco, estoque):
        produto = Produto(0, descricao, preco, estoque)
        Produtos.inserir(produto)

    @staticmethod
    def produtoAtualizar(id, descricao, preco, estoque):
        produto = Produto(id, descricao, preco, estoque)
        Produtos.atualizar(produto)

    @staticmethod
    def produtoExcluir(id):
        Produtos.excluir(Produtos.listarId(id))

    @staticmethod
    def categoriaListar():
        return Categorias.listar()
    
    @staticmethod
    def categoriaInserir(descricao):
        categoria = Categoria(0, descricao)
        Categorias.inserir(categoria)

    @staticmethod
    def categoriaAtualizar(id, descricao):
        categoria = Categoria(id, descricao)
        Categorias.atualizar(categoria)

    @staticmethod
    def categoriaExcluir(id):
        Categorias.excluir(Categorias.listarId(id))

    @staticmethod
    def clienteListar():
        return Clientes.listar()
    
    @staticmethod
    def clienteInserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        Clientes.inserir(cliente)

    @staticmethod
    def clienteAtualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        Clientes.atualizar(cliente)

    @staticmethod
    def clienteExcluir(id):
        Clientes.excluir(Clientes.listar_id(id))