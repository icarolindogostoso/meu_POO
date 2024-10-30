class Frete:
    def __init__ (self, distancia, peso):
        self.setDistancia(distancia)
        self.setPeso(peso)
        
    def setDistancia (self, v):
        if v > 0:
            self.__distancia = v
        else:
            raise ValueError("Distancia negativa")
    
    def setPeso (self, v):
        if v >= 0:
            self.__peso = v
        else:
            raise ValueError("Peso invalido")
        
    def getDistancia (self):
        return self.__distancia

    def getPeso (self):
        return self.__peso
    
    def calcFrete (self):
        return self.__peso / self.__distancia * 100
    
    def __str__ (self):
        return f"Frete de distancia {self.__distancia} e peso {self.__peso}"
    
class UI:
    def main():
        peso = float(input("Infome o peso: "))
        distancia = float(input("Informe a distancia: "))

        x = Frete(distancia, peso)

        print(x)
        print(f"Frete = {x.calcFrete()}")

UI.main()
    