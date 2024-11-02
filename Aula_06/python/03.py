class Conversor:
    def __init__ (self, num):
        self.setNum(num)

    def setNum (self, num):
        if num > 0:
            self.__num = num
        else:
            raise ValueError ("Valor negativo")
        
    def getNum (self):
        return self.__num
    
    def binario (self):
        binario = ""
        numero = self.__num 
        while numero > 0:
            binario = str(numero%2) + binario
            numero = numero//2
        return binario
    
    def __str__(self) :
        return f'Convertendo o numero {self.__num} para binario'
    

class UI:
    @staticmethod
    def main():
        numero = int(input("Informe um numero: "))
        x = Conversor(numero)
        print(x.getNum())
        print(x.binario())
        print(x)

UI.main()