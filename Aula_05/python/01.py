import math

class Circulo:
    def __init__ (self):
        self.__raio = 0

    def set_raio (self, v):
        if v > 0:
            self.__raio = v
        else:
            raise ValueError ("A base do triangulo nao pode ser negativa")
        
    def get_raio (self):
        return self.__raio
    
    def calc_area (self):
        return self.__raio ** 2 * math.pi
    
    def calc_circunferencia (self):
        return 2 * math.pi * self.__raio
    

class UI:
    @staticmethod
    def main():
        x = Circulo()

        x.set_raio(float(input("Informe o valor do raio do circulo: ")))

        print(f"Raio = {x.get_raio()}")
        print(f"Area = {x.calc_area():.2f}")
        print(f"Circunferencia = {x.calc_circunferencia():.2f}")
        
UI.main()