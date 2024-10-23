class Triangulo:
    def __init__ (self):
        self.b = 0
        self.h = 0
    def calc_area (self):
        return self.b * self.h / 2

class UI:
    @staticmethod
    def main(){
        x = Triangulo()
        x.b = 10
        x.h = 20
        print(x.calc_area())
    }