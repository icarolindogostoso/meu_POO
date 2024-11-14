import json
from datetime import datetime

class Venda:
    def __init__ (self, id):
        self.setId(id)
        self.setData()
        self.setCarrinho()
        self.setTotal()
        self.setIdCliente()

    def setId (self, id):
        if id > 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
    
    def setData (self, data = None):
        if data == None:
            self.__data = datetime.today()
        else:
            self.__data = data

    def setCarrinho (self):
        self.__carrinho = False

    def setTotal (self):
        self.__total = 0.0

    def setIdCliente (self):
        self.__idCliente = 0

    def getId(self):
        return self.__id

    def getData(self):
        return self.__data.date()

    def getCarrinho (self):
        return self.__carrinho

    def getTotal(self):
        return self.__total

    def getIdCliente(self):
        return self.__idCliente
        
    def __str__ (self):
        return f"{self.__id} - {self.__data.date()} - {self.__carrinho} - {self.__total} - {self.__idCliente}"
    
class Vendas:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.abrir()

        id = 0
        for venda in cls.objetos:
            if venda.getId() > id:
                id = venda.getId()
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
        for venda in cls.objetos:
            if venda.getId() == id:
                return venda
        return None
            
    @classmethod
    def atualizar (cls, obj):
        venda = cls.listarId(obj.getId())
        if venda != None:
            venda.setData(cls.getData())
            venda.setCarrinho()
            venda.setTotal()
            venda.setIdCliente()
        cls.salvar()

    @classmethod
    def excluir (cls, obj):
        venda = cls.listarId(obj.getId())
        if venda != None:
            cls.objetos.remove(venda)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Aula_09/Projeto_2/vendas.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Venda(obj["id"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Aula_09/Projeto_2/vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)