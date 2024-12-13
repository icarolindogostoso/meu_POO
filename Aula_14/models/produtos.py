import json

class Produto:
    def __init__ (self, id, d, p, e, i):
        self.setId(id)
        self.setDescricao(d)
        self.setPreco(p)
        self.setEstoque(e)
        self.setIdCategoria(i)

    def setId (self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
        
    def setDescricao (self, d):
        if len(d) > 0:
            self.__descricao = d
        else:
            raise ValueError ("Descricao invalida")
        
    def setPreco (self, p):
        if p > 0:
            self.__preco = p
        else:
            raise ValueError ("Preco invalido")
        
    def setEstoque (self, e):
        if e >= 0:
            self.__estoque = e
        else:
            raise ValueError ("Estoque invalido")
        
    def setIdCategoria (self, i):
        self.__idCategoria = i

    def getId (self):
        return self.__id
    
    def getDescricao (self):
        return self.__descricao
    
    def getPreco (self):
        return self.__preco
    
    def getEstoque (self):
        return self.__estoque
    
    def getIdCategoria (self):
        return self.__idCategoria

    def __str__ (self):
        return f"{self.__id} - {self.__descricao} - {self.__preco} - {self.__estoque} - {self.__idCategoria}"
    
class Produtos:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.abrir()

        id = 0
        for produto in cls.objetos:
            if produto.getId() > id:
                id = produto.getId()
        obj.setId(id + 1)

        cls.objetos.append(obj)

        cls.salvar()

    @classmethod
    def listar (cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listarId (cls, id):
        cls.abrir()

        for produto in cls.objetos:
                if produto.getId() == id:
                    return produto
        return None
                
    @classmethod
    def atualizar (cls, obj):
        produto = cls.listarId(obj.getId())
        if produto != None:
            produto.setDescricao(obj.getDescricao())
            produto.setPreco(obj.getPreco())
            produto.setEstoque(obj.getEstoque())
            produto.setIdCategoria(obj.getIdCategoria())
            cls.salvar()

    @classmethod
    def excluir (cls, obj):
        produto = cls.listarId(obj.getId())
        if produto != None:
            cls.objetos.remove(produto)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Produto(obj["_Produto__id"], obj["_Produto__descricao"], obj["_Produto__preco"], obj["_Produto__estoque"], obj["_Produto__idCategoria"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)