from abc import ABC, abstractmethod
import math

class Figura(ABC):
    def __init__ (self, cor):
        super().__init__()
        self.__cor = cor

    def getCor (self):
        return self.__cor

    @abstractmethod
    def getArea (self):
        pass


class Circulo (Figura):
    def __init__ (self, cor, raio):
        super().__init__(cor)
        self.__r = raio

    def getArea (self):
        return math.pi * self.__r ** 2


class Triangulo (Figura):
    def __init__ (self, cor, base, altura):
        super().__init__ (cor)
        self.__b = base
        self.__h = altura

    def getArea (self):
        return self.__b * self.__h / 2