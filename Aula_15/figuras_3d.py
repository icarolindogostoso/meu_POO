from abc import ABC, abstractmethod

class Figura3D (ABC):
    @abstractmethod
    def get_volume (self) -> float:
        pass

class Esfera (Figura3D):
    def __init__ (self, raio : float):
        self.__raio = raio

    def get_volume(self) -> float:
        return 