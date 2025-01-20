import json
from abc import ABC, abstractmethod

class Modelo (ABC):
    objetos = []

    @classmethod
    def inserir(cls, obj : object):
        cls.abrir()

        id = 0
        for objeto in cls.objetos:
            if objeto.getId():
                id = objeto.getId()
        obj.setId(id + 1)

        cls.objetos.append(obj)

        cls.salvar()

    @classmethod
    def listar (cls) -> list:
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id (cls, id : int) -> object:
        cls.abrir()

        for objeto in cls.objetos:
            if objeto.getId() == id:
                return objeto
        return None
    
    @classmethod
    @abstractmethod
    def atualizar (cls, obj : object):
        pass

    @classmethod
    def excluir (cls, obj : object):
        objeto = cls.listar_id(obj.getId())
        if objeto != None:
            cls.objetos.remove(objeto)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open('''''', mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Modelo('''''')
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('''''', mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)