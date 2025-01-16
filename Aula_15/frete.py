class Frete:
    def __init__ (self, d : float, p : float):
        self.__distancia = d
        self.__peso = p

    def get_distancia (self) -> float:
        return self.__distancia

    def get_peso (self) -> float:
        return self.__peso

    def valor_frete (self) -> float:
        return self.__distancia * self.__peso

    def __str__ (self) -> str:
        return f"{self.__distancia} - {self.__peso}"

class FreteExpresso (Frete):
    def __init__ (self, d : float, p : float, s : int):
        super().__init__ (d, p)
        self.__seguro = s

    def get_seguro (self) -> int:
        return self.__seguro

    def valor_frete (self) -> float:
        return super().valor_frete() + self.__seguro * 0.01

    def __str__ (self) -> str:
        return f"{super().get_distancia()} - {super().get_peso()} - {self.__seguro}"

x = Frete(10, 20)
y = FreteExpresso (10, 20, 1000)

print(x.get_distancia())
print(x.get_peso())
print(x.valor_frete())
print(x)
print(type(x))
print(isinstance(x, object))
print(isinstance(x, Frete))
print(isinstance(x, FreteExpresso))

print(y.get_distancia())
print(y.get_peso())
print(y.get_seguro())
print(y.valor_frete())
print(y)
print(type(y))
print(isinstance(y, object))
print(isinstance(y, Frete))
print(isinstance(y, FreteExpresso))