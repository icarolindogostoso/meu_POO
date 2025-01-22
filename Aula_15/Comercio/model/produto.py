from model.cliente import Modelo
import json

class Produto:
    def __init__ (self, id, f, n, d, p, e, i):
        self.setId(id)
        self.setFoto(f)
        self.setNome(n)
        self.setDescricao(d)
        self.setPreco(p)
        self.setEstoque(e)
        self.setIdCategoria(i)

    def setId (self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
        
    def setFoto (self, f):
        if len(f) >= 0:
            self.__foto = f
        else:
            raise ValueError ("Foto invalida")
        
    def setNome (self, n):
        if len(n) >= 0:
            self.__nome = n
        else:
            raise ValueError ("Nome invalido")
        
    def setDescricao (self, d):
        if len(d) >= 0:
            self.__descricao = d
        else:
            raise ValueError ("Descricao invalida")
        
    def setPreco (self, p):
        if p >= 0:
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
    
    def getFoto (self):
        return self.__foto
    
    def getNome (self):
        return self.__nome
    
    def getDescricao (self):
        return self.__descricao
    
    def getPreco (self):
        return self.__preco
    
    def getEstoque (self):
        return self.__estoque
    
    def getIdCategoria (self):
        return self.__idCategoria

    def __str__ (self):
        return f"id: {self.__id} - produto: {self.__nome} - preço: {self.__preco:.2f} - estoque: {self.__estoque}"
    
class Produtos(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Projeto/produtos.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Produto(obj["_Produto__id"], obj["_Produto__foto"], obj["_Produto__nome"], obj["_Produto__descricao"], obj["_Produto__preco"], obj["_Produto__estoque"], obj["_Produto__idCategoria"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Projeto/produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)