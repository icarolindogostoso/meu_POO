from abc import ABC, abstractmethod
import math

class Figura3D (ABC):
    @abstractmethod
    def get_volume (self) -> float:
        pass

class Esfera (Figura3D):
    def __init__ (self, raio : float):
        self.__raio = raio

    def get_volume(self) -> float:
        return (4*math.pi*(self.__raio**3))/3
    
class Cubo (Figura3D):
    def __init__ (self, lado : float):
        self.__lado = lado

    def get_volume(self) -> float:
        return self.__lado ** 3