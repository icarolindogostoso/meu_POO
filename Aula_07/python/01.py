import random

class Bingo:
    def __init__(self, numbolas) :
        self.__setNumBolas(numbolas)
        self.__bolas = list(range(1, self.__numbolas + 1))
        self.__bolasSorteadas = []

    def __setNumBolas (self, valor):
        if valor > 0:
            self.__numbolas = valor
        else:
            raise ValueError ("Bolas negativas")
    
    def proximo (self):
        bolasorteada = random.choice(self.__bolas)
        self.__bolasSorteadas.append(bolasorteada)
        self.__bolas.remove(bolasorteada)
        return bolasorteada

    def numerosParaSortear (self):
        return self.__bolas
    
    def sorteados (self):
        return self.__bolasSorteadas


class UI:
    @staticmethod
    def main():
        numero = int(input("Numero de bolas: "))
        x = Bingo(numero)
        print(x.numerosParaSortear())
        print(x.proximo())
        print(x.numerosParaSortear())
        print(x.sorteados())

UI.main()