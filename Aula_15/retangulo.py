import math
from tkinter.messagebox import YES

class Retangulo:
    def __init__ (self, b, h):
        self.__b = b
        self.__h = h

    def get_base (self):
        return self.__b

    def get_altura (self):
        return self.__h

    def calc_area (self):
        return self.__b * self.__h

    def calc_diagonal (self):
        return math.sqrt(self.__b ** 2 + self.__h ** 2)

    def __str__ (self):
        return f"Retangulo de base {self.__b} e altura {self.__h}"


class Quadrado (Retangulo):
    def __init__ (self, l):
        super().__init__ (l, l)

    def __str__ (self):
        return f"Quadrado de lado {self.get_base()}"

x = Retangulo(10, 20)
y = Quadrado (10)

print(x.get_base())
print(x.get_altura())
print(x.calc_area())
print(x.calc_diagonal())
print(x)
print(type(x))
print(isinstance(x, object))
print(isinstance(x, Retangulo))
print(isinstance(x, Quadrado))

print(y.get_base())
print(y.get_altura())
print(y.calc_area())
print(y.calc_diagonal())
print(y)
print(type(y))
print(isinstance(y, object))
print(isinstance(y, Retangulo))
print(isinstance(y, Quadrado))