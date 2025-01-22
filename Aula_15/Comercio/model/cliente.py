from model.cliente import Modelo
import json

class Cliente:
    def __init__ (self, id, nome, email, fone, senha):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setFone(fone)
        self.setSenha(senha)

    def setId (self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
        
    def setNome (self, n):
        if len(n) >= 0:
            self.__nome = n
        else:
            raise ValueError ("Nome invalido")
        
    def setEmail (self, e):
        if len(e) >= 0:
            self.__email = e
        else:
            raise ValueError ("Email invalido")
        
    def setFone (self, f):
        if len(f) >= 0:
            self.__fone = f
        else:
            raise ValueError ("Nome invalido")
        
    def setSenha (self, s):
        if len(s) >= 0:
            self.__senha = s
        else:
            raise ValueError ("Senha invalida")
        
    def getSenha (self, s):
        if len(s) >= 0:
            self.__senha = s
        else:
            raise ValueError ("Senha invalida")
        
    def getId (self):
        return self.__id
    
    def getNome (self):
        return self.__nome
    
    def getEmail (self):
        return self.__email
    
    def getFone (self):
        return self.__fone
    
    def getSenha (self):
        return self.__senha
        
    def __str__ (self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    
class Clientes (Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Projeto/clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"], obj["_Cliente__senha"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Projeto/clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)