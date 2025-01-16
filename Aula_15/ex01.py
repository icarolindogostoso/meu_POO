class Funcionario:
    def __init__ (self, nome, salarioBase):
        self.__nome = nome
        self._salarioBase = salarioBase
    
    def getNome (self):
        return self.__nome

    def getSalario (self):
        return self._salarioBase

    def __str__ (self):
        return f"{self.__nome} - {self.getSalario()}"


class Gerente (Funcionario):
    def __init__ (self, nome, salarioBase, gratificacao):
        super().__init__ (nome, salarioBase)
        self.__gratificacao = gratificacao

    def getSalario(self):
        return super().getSalario() + self.__gratificacao


x = Funcionario("José Maria", 5000)
y = Gerente("Maria José", 5000, 3000)

print(x.getNome()) # José Maria
print(x.getSalario()) # 5000
print(x) # José Maria - 5000
print(type(x)) # <class '__main__.Funcionario'>
print(isinstance(x, object)) # True
print(isinstance(x, Funcionario)) # True
print(isinstance(x, Gerente)) # False

print(y.getNome()) # Maria José
print(y.getSalario()) # 8000
print(y) # Maria José - 8000
print(type(y)) # <class '__main__.Gerente'>
print(isinstance(y, object)) # True
print(isinstance(y, Funcionario)) # True
print(isinstance(y, Gerente)) # True