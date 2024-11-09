import json

class Cliente:
    def __init__ (self, id, n, e, f):
        self.setId(id)
        self.setNome(n)
        self.setEmail(e)
        self.setFone(f)

    def setId (self, id):
        if id > 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
        
    def setNome (self, n):
        if len(n) > 0:
            self.__nome = n
        else:
            raise ValueError ("Nome invalido")
        
    def setEmail (self, e):
        if len(e) > 0:
            self.__email = e
        else:
            raise ValueError ("Email invalido")
        
    def setFone (self, f):
        if len(f) > 0:
            self.__fone = f
        else:
            raise ValueError ("Nome invalido")
        
    def getId (self):
        return self.__id
    
    def getNome (self):
        return self.__nome
    
    def getEmail (self):
        return self.__email
    
    def getFone (self):
        return self.__nome
        
    def __str__ (self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
        
class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar(cls):
        return cls.objetos
    
    @classmethod
    def listarId(cls, id):
        for cliente in cls.objetos:
            if cliente.getId() == id:
                return cliente
    
    @classmethod
    def atualizar (cls, obj):
        for i, cliente in enumerate(cls.objetos):
            if cliente.getId() == obj.getId():
                cls.objetos[i] = obj

    @classmethod
    def excluir (cls, obj):
        for i, cliente in enumerate(cls.objetos):
            if cliente.getId() == obj.getId():
                del cls.objetos[i]

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("Aula_09/clientes.json", mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                cls.objetos.append(c)

    @classmethod
    def salvar(cls):
        with open("Aula_09/clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)