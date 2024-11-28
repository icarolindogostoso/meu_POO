from datetime import datetime, timedelta

class Treino:
    def __init__ (self, id, id_atleta, data, distancia, tempo):
        self.__id = id
        self.__id_atleta = id_atleta
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo
        if distancia < 0:
            raise ValueError ("Distancia invalida")

    def get_id_atleta (self):
        return self.__id_atleta

    def pace (self):
        # t2 = (self.__tempo.hour * 60) + self.__tempo.minute + (self.__tempo.second / 60)
        t = self.__tempo.total_seconds() / 60
        d = self.__distancia / 1000
        return t/d        

    def __str__ (self):
        return f"{self.__id} - {self.__id_atleta} - {self.__data.strftime('%d/%m/%Y')} - {self.__distancia}m - {self.__tempo}"

class Treinos:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar (cls):
        return cls.objetos