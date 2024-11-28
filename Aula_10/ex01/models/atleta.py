from datetime import datetime

class Atleta:
    def __init__ (self, id, nome, nascimento):
        self.__id = id
        self.__nome = nome
        self.__nascimento = nascimento
        if nome == "": 
            raise ValueError ("Nome invalido")

    def __str__ (self):
        return f"{self.__id} - {self.__nome} - {self.__nascimento.strftime('%d/%m/%Y')}"

class Atletas:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar (cls):
        return cls.objetos