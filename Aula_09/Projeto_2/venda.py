import json
from datetime import datetime

class Venda:
    def __init__ (self, id):
        self.setId(id)
        self.__data = datetime.today()
        self.setCarrinho()
        self.setTotal()
        self.setIdCliente()

    def setId (self, id):
        if id > 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
        
    def setCarrinho (self):
        self.__carrinho = False

    def setTotal (self):
        self.__total = 0.0

    def setIdCliente (self):
        self.__idCliente = 0
        
    def __str__ (self):
        return f"{self.__id} - {self.__data.date()} - {self.__carrinho} - {self.__total} - {self.__idCliente}"
    
class Vendas:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar (cls):
        return cls.objetos
    
    @classmethod
    def listarId (cls, id):
        for venda in cls.objetos:
            if venda.getId() == id:
                return venda
            
    @classmethod
    def atualizar (cls, obj):
        for i, venda in enumerate(cls.objetos):
            if venda.getId() == obj.getId():
                cls.objetos[i] = obj

    @classmethod
    def excluir (cls, obj):
        for i, venda in enumerate(cls.objetos):
            if venda.getId() == obj.getId():
                del cls.objetos[i]

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("Aula_09/clientes.json", mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Venda(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.objetos.append(c)

    @classmethod
    def salvar(cls):
        with open("Aula_09/clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)