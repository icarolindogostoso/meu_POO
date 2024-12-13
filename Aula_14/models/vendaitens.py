import json

class VendaItem:
    def __init__ (self, id, q, p, iv, ip):
        self.setId(id)
        self.setQtd(q)
        self.setPreco(p)
        self.setIdVenda(iv)
        self.setIdProduto(ip)

    def setId (self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
        
    def setQtd (self, q):
        if q > 0:
            self.__qtd = q
        else:
            raise ValueError ("Quantidade invalida")
        
    def setPreco (self, p):
        if p > 0:
            self.__preco = p
        else:
            raise ValueError ("Preco invalido")
        
    def setIdVenda(self, iv):
        self.__idVenda = iv

    def setIdProduto (self, ip):
        self.__idProduto = ip

    def getId (self):
        return self.__id
    
    def getQtd (self):
        return self.__qtd
    
    def getPreco (self):
        return self.__preco

    def getIdVenda (self):
        return self.__idVenda
    
    def getIdProduto (self):
        return self.__idProduto

    def __str__ (self):
        return f"{self.__id} - {self.__qtd} - {self.__preco} - {self.__idVenda} - {self.__idProduto}"
    
class VendaItens:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.abrir()

        id = 0
        for vendaitem in cls.objetos:
            if vendaitem.getId() > id:
                id = vendaitem.getId()
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

        for vendaitem in cls.objetos:
            if vendaitem.getId() == id:
                return vendaitem
        return None
    
    @classmethod
    def atualizar (cls, obj):
        vendaitem = cls.listarId(obj.getId())
        if vendaitem != None:
            vendaitem.setQtd(obj.getQtd())
            vendaitem.setPreco(obj.getPreco())
            vendaitem.setIdVenda(obj.getIdVenda())
            vendaitem.setIdProduto(obj.getIdProduto())
            cls.salvar()

    @classmethod
    def excluir (cls, obj):
        vendaitem = cls.listarId(obj.getId())
        if vendaitem != None:
            cls.objetos.remove(vendaitem)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendaitens.json", mode="r") as arquivo:
                produtos_json = json.load(arquivo)
                for obj in produtos_json:
                    c = VendaItem(obj["_VendaItem__id"], obj["_VendaItem__qtd"], obj["_VendaItem__preco"], obj["_VendaItem__idVenda"], obj["_VendaItem__idProduto"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar (cls):
        with open("vendaitens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)