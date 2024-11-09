import json

class Produto:
    def __init__ (self, id, d, p, e):
        self.setId(id)
        self.setDescricao(d)
        self.setPreco(p)
        self.setEstoque(e)
        self.setIdCategoria()

    def setId (self, id):
        if id > 0:
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
        if e > 0:
            self.__estoque = e
        else:
            raise ValueError ("Estoque invalido")
        
    def setIdCategoria (self):
        self.__idCategoria = 0

    def getId (self):
        return self.__id

    def __str__ (self):
        return f"{self.__id} - {self.__descricao} - {self.__preco} - {self.__estoque} - {self.__idCategoria}"
    
class Produtos:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar (cls):
        return cls.objetos
    
    @classmethod
    def listarId (cls, id):
        for produto in cls.objetos:
                if produto.getId() == id:
                    return produto
                
    @classmethod
    def atualizar (cls, obj):
        for i, produto in enumerate(cls.objetos):
            if produto.getId() == obj.getId():
                cls.objetos[i] = obj

    @classmethod
    def excluir (cls, obj):
        for i, produto in enumerate(cls.objetos):
            if produto.getId() == obj.getId():
                del cls.objetos[i]

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("Aula_09/Projeto_2/produtos.json", mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Produto(obj["id"], obj["d"], obj["p"], obj["e"])
                cls.objetos.append(c)

    @classmethod
    def salvar(cls):
        with open("Aula_09/Projeto_2/produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)