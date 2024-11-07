class Cliente:
    def __init__ (self, id, nome):
        self.id = id
        self.nome = nome

    def __str__ (self):
        return f"{self.id} - {self.nome}"

a = Cliente(1, "Icaro")
b = Cliente(2, "Gustavo")

print(a)
print(b)

print(a.__dict__)
print(b.__dict__)

print(vars(a))
print(vars(b))