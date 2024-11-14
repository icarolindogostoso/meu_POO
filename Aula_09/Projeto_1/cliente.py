import json

class Cliente:
    def __init__ (self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__ (self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    
class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id:
                id = x.id
        obj.id = id + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.objetos:
            if x.id == id:
                return x
        return None
    
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            x.nome = obj.nome
            x.email = obj.email
            x.fone = obj.fone
        cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
    
    @classmethod
    def salvar(cls):
        with open("Aula_09/Projeto_1/clientela.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Aula_09/Projeto_1/clientela.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass