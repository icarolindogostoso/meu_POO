class Retangulo:
    def __init__ (self,b, h):
        self.setBase(b)
        self.setAltura(h)

    def setBase (self, v):
        if v > 0:
            self.__b = v
        else:
            raise ValueError ("a base do retangulo não pode ser negativa")

    def setAltura (self, v):
        if v > 0:
            self.__h = v
        else:
            raise ValueError ("a altura do retangulo não pode ser negativa")
    
    def getBase (self):
        return self.__b
    
    def getAltura (self):
        return self.__h
    
    def calcArea (self):
        return self.__b * self.__h
    
    def calcDiagonal (self):
        return (self.__b ** 2 + self.__h ** 2) ** 0.5
    
    def __str__ (self):
        return f"Eu sou um retangulo de base {self.__b} e altura {self.__h}"


class UI:
    def main():
        b = float(input("Informe o valor da base do retangulo: "))
        h = float(input("Informe o valor da altura do retangulo: "))

        x = Retangulo(b,h)

        print(x)
        print(f"Area = {x.calcArea()}")
        print(f"Diagonal = {x.calcDiagonal():.2f}")        

UI.main()