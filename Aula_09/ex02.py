import json

class Cliente:
    def __init__ (self, id, nome):
        self.id = id
        self.nome = nome

    def __str__ (self):
        return f"{self.id} - {self.nome}"

def salvar():
    a = Cliente(1, "Icaro")
    b = Cliente(2, "Gustavo")

    print(a)
    print(b)

    print(a.__dict__)
    print(b.__dict__)

    print(vars(a))
    print(vars(b))

    clientes = [a, b]
    with open("Aula_09/clientes.json", mode="w") as arquivo:
        json.dump(clientes, arquivo, default = vars)

def abrir():
    clientes = []
    with open("Aula_09/clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
            c = Cliente(obj["id"], obj["nome"])
            clientes.append(c)

    for c in clientes:
        print(c)

abrir()