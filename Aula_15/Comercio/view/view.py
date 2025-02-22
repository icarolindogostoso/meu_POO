from model.cliente import Cliente, Clientes
from model.categoria import Categoria, Categorias
from model.produto import Produto, Produtos
from model.venda import Venda, Vendas
from model.vendaitem import VendaItem, VendaItens

class View:
    @staticmethod
    def clienteAdmin():
        for c in Clientes.listar():
            if c.getEmail() == "admin":
                return None
        View.clienteInserir("admin", "admin", "0000", "1234")

    @staticmethod
    def clienteAutenticar(email, senha):
        for c in Clientes.listar():
            if c.getEmail() == email and c.getSenha() == senha:
                return {"id" : c.getId(), "nome" : c.getNome()}
        return None

    @staticmethod
    def clienteListar():
        return Clientes.listar()
    
    @staticmethod
    def clienteInserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)

    @staticmethod
    def clienteAtualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)
    
    @staticmethod
    def clienteExcluir(id):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)

    @staticmethod
    def categoriaListar():
        return Categorias.listar()

    @staticmethod
    def categoriaListarId(id):
        return Categorias.listar_id(id)
    
    @staticmethod
    def categoriaInserir(nome, descricao):
        c = Categoria(0, nome, descricao)
        Categorias.inserir(c)

    @staticmethod
    def categoriaAtualizar(id, nome, descricao):
        c = Categoria(id, nome, descricao)
        Categorias.atualizar(c)
    
    @staticmethod
    def categoriaExcluir(id):
        c = Categoria(id, "")
        Categorias.excluir(c)

    @staticmethod
    def produtoListar():
        return Produtos.listar()
    
    @staticmethod
    def produtoInserir(foto, nome, descricao, preco, estoque, id_categoria):
        c = Produto(0, foto, nome, descricao, preco, estoque, id_categoria)
        Produtos.inserir(c)

    @staticmethod
    def produtoAtualizar(id, foto, nome, descricao, preco, estoque, id_categoria):
        c = Produto(id, foto, nome, descricao, preco, estoque, id_categoria)
        Produtos.atualizar(c)
    
    @staticmethod
    def produtoExcluir(id):
        c = Produto(id, "", 0, 0, None)
        Produtos.excluir(c)

    @staticmethod
    def produtoReajustarTodos(percentual):
        for obj in View.produtoListar():
            View.produtoAtualizar(obj.getId(), obj.getFoto(), obj.getNome(), obj.getDescricao(), obj.getPreco() * (1 + percentual), obj.getEstoque(), obj.getIdCategoria())

    @staticmethod
    def produtoReajustarEspecifico(id, percentual):
        obj = Produtos.listarId(id)
        View.produtoAtualizar(obj.getId(), obj.getFoto(), obj.getNome(), obj.getDescricao(), obj.getPreco() * (1 + percentual), obj.getEstoque(), obj.getIdCategoria())

    @staticmethod
    def vendaInserir(carrinho, total, id_cliente):
        ativo = False
        for venda in Vendas.listar():
            if venda.getIdCliente() == id_cliente and venda.getCarrinho() == True:
                ativo = True
                break
        if ativo == False:
            v = Venda(0, None, carrinho, total, id_cliente)
            Vendas.inserir(v)

    @staticmethod
    def vendaFechar(id_cliente):
        id_venda = 0
        for venda in Vendas.listar():
            if venda.getIdCliente() == id_cliente and venda.getCarrinho() == True:
                id_venda = venda.getId()
                id = venda.getId()
                carrinho = False
                total = venda.getTotal()
                id_cliente = venda.getIdCliente()
                data = venda.getData()
                v = Venda(id, data, carrinho, total, id_cliente)
                Vendas.atualizar(v)
                break
        
        for vendaitem in VendaItens.listar():
            id_produto = 0
            if vendaitem.getIdVenda() == id_venda:
                id_produto = vendaitem.getIdProduto()

            for produto in Produtos.listar():
                if produto.getId() == id_produto:
                    estoque = produto.getEstoque()
                    estoque = estoque + vendaitem.getQtd()
                    View.produtoAtualizar(produto.getId(), produto.getFoto(), produto.getNome(), produto.getDescricao(), produto.getPreco(), estoque , produto.getIdCategoria())
                    break

    @staticmethod
    def vendaListar():
        return Vendas.listar()
    
    @staticmethod
    def vendaAtualizar(id, data, carrinho, total, id_cliente):
        v = Venda(id, data, carrinho, total, id_cliente)
        Vendas.atualizar(v)
    
    @staticmethod
    def vendaItemInserir(nome, quantidade, preco, id_venda, id_produto):
        v = VendaItem(0, nome, quantidade, preco, id_venda, id_produto)
        VendaItens.inserir(v)

    @staticmethod
    def vendaItemListar():
        return VendaItens.listar()
    
    @staticmethod
    def vendaItemExcluir(id):
        v = VendaItem(id, "", 0, 0, None, None)
        VendaItens.excluir(v)

    @staticmethod
    def vendaItemAtualizar(id, nome, quantidade, preco, id_venda, id_produto):
        v = VendaItem(id, nome, quantidade, preco, id_venda, id_produto)
        VendaItens.atualizar(v)