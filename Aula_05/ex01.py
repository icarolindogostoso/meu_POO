import math

class Triangulo:
    def __init__ (self):
        self.__b = 0
        self.__h = 0

    def set_base (self, v):
        if v > 0:
            self.__b = v
        else:
            raise ValueError ("a base do triangulo não pode ser negativa")

    def set_altura (self, v):
        if v > 0:
            self.__h = v
        else:
            raise ValueError ("a altura do triangulo não pode ser negativa")

    def get_base (self):
        return self.__b

    def get_altura (self):
        return self.__h

    def calc_area (self):
        return self.__b * self.__h / 2


class Circulo:
    def __init__ (self):
        self.raio = 0

    def calc_area (self):
        return self.raio ** 2 * math.pi


class UI:
    @staticmethod
    def main():
        op = 1
        while op != 0:
            op = UI.menu()
            if op == 1:
                UI.novo_triangulo()
            if op == 2:
                UI.novo_circulo()

    @staticmethod
    def menu():
        print("1-Triangulo   2-Circulo   0-Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def novo_triangulo():
        x = Triangulo()
        #x.b = float(input("Informe o vlaor da base do triangulo: "))
        #x.h = float(input("Informe o valor da altura: "))

        x.set_base(float(input("Informe o valor da base do triangulo: ")))
        x.set_altura(float(input("Informe o valor da altura: ")))

        #print(f"Base = {x.__b}, Altura = {x.__h}")

        print(f"Base = {x.get_base()}, Altura = {x.get_altura()}")
        print(f"Area = {x.calc_area()}")

    @staticmethod
    def novo_circulo():
        x = Circulo()
        x.raio = float(input("Informe o valor do raio do circulo: "))
        print(f"Area = {x.calc_area()}")
    
UI.main()