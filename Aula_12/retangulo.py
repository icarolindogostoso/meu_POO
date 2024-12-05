import math

class Retangulo:
    def __init__ (self, b, h):
        self.__b = b
        self.__h = h

    def __str__ (self):
        return f"base = {self.__b}, altura = {self.__h}"
    
    def calcArea (self):
        return self.__b * self.__h
    
    def calcDiagonal (self):
        return math.sqrt(self.__b ** 2 + self.__h ** 2)