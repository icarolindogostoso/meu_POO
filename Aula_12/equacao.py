import math

class Equacao:
    def __init__ (self, a, b, c):
        self.setA(a)
        self.setB(b)
        self.setC(c)

    def setA (self, a):
        if a == 0:
            raise ValueError ("o A nao pode ser 0 em uma equacao de 2 grau")
        self.__a = a
    def setB (self, b):
        self.__b = b
    def setC (self, c):
        self.__c = c

    def getA (self):
        return self.__a
    def getB (self):
        return self.__b
    def getC (self):
        return self.__c

    def Delta (self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def Y (self, x):
        return self.__a * (x ** 2) + self.__b * x + self.__c
    
    def X1 (self):
        if (self.Delta()) < 0:
            return None
        return ((self.__b * -1) - math.sqrt(self.Delta())) / (2 * (self.__a))
    
    def X2 (self):
        if (self.Delta()) < 0:
            return None
        return ((self.__b * -1) + math.sqrt(self.Delta())) / (2 * (self.__a))
    
    def XVertice(self):
        return (self.__b * -1) / (2 * self.__a)

    def __str__ (self):
        return f"{self.__a} - {self.__c} - {self.__c}"