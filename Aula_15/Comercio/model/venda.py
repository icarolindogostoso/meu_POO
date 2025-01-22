from model.cliente import Modelo
import json
from datetime import datetime

class Venda:
    def __init__ (self, id, d, c, t, i):
        self.setId(id)
        self.setData(d)
        self.setCarrinho(c)
        self.setTotal(t)
        self.setIdCliente(i)

    def setId (self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
    
    def setData (self, data):
        if data != None:
            self.__data = data
        else:
            dia = datetime.today()
            self.__data = dia.isoformat()


    def setCarrinho (self, carrinho):
        if type(carrinho) == bool:
            self.__carrinho = carrinho
        else:
            raise ValueError ("Carrinho invalido")

    def setTotal (self, total):
        if total >= 0:
            self.__total = total
        else:
            raise ValueError ("Total invalido")

    def setIdCliente (self, idCliente):
        self.__idCliente = idCliente

    def getId(self):
        return self.__id

    def getData(self):
        return self.__data

    def getCarrinho (self):
        return self.__carrinho

    def getTotal(self):
        return self.__total

    def getIdCliente(self):
        return self.__idCliente
        
    def __str__ (self):
        return f"{self.__id} - {self.__data} - {self.__carrinho} - {self.__total} - {self.__idCliente}"
    
class Vendas (Modelo):
        @classmethod
        def abrir(cls):
            cls.objetos = []
            try:
                with open("Projeto/vendas.json", mode="r") as arquivo:
                    clientes_json = json.load(arquivo)
                    for obj in clientes_json:
                        c = Venda(obj["_Venda__id"], obj["_Venda__data"], obj["_Venda__carrinho"], obj["_Venda__total"], obj["_Venda__idCliente"])
                        cls.objetos.append(c)
            except FileNotFoundError:
                pass

        @classmethod
        def salvar(cls):
            with open("Projeto/vendas.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default = vars)