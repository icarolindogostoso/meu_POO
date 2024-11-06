class Empresa:
    def __init__ (self, nome):
        self.__nome = nome
        self.__clientes = []
        if nome == "":
            raise ValueError ("Nome invalido")
            
    def inserir (self, c):
        self.__clientes.append(c)

    def listar(self):
        return self.__clientes

    def __str__ (self):
        return f"Empresa {self.__nome} tem {len(self.__clientes)} cliente(s)"

class Cliente:
    def __init__ (self, nome, cpf, limite):
        self.__nome = nome
        self.__cpf = cpf
        self.__limite = limite
        self.__socio = None
        if nome == "": 
            raise ValueError ("Nome invalido")
        if cpf == "": 
            raise ValueError ("Cpf invalido")
        if limite < 0 : 
            raise ValueError ("Limite invalido")

    def set_socio(self, c):
        if self == c:
            raise ValueError ("Não pode ser sócio dele mesmo")
        if self.__socio != None: 
            self.__socio.__socio = None
        if c.__socio != None:
            c.__socio.__socio = None
        self.__socio = c
        c.__socio = self
        # if self.__socio != None:
        #     self.__socio.set_socio(None)

    def get_limite(self):
        if self.__socio == None:
            return self.__limite
        else:
            return self.__limite + self.__socio.__limite

    def __str__ (self):
        s =  f"{self.__nome} - {self.__cpf} "
        s = s + f"Limite individual = {self.__limite} - "
        s = s + f"Limite total = {self.get_limite()} "
        if self.__socio != None: 
            s = s + f"Sócio = {self.__socio.__nome}"
        return s

class UI:
    empresa = None
    def menu():
        print("1 - Nova empresa, 2 - Mostrar empresa, 3 - Inserir cliente, 4 - Listar clientes, 5 - Sociedade, 9 - Fim")
        return int(input("Informe uma opção: "))

    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.nova_empresa()
            if op == 2:
                UI.mostrar_empresa()
            if op == 3:
                UI.inserir_cliente()
            if op == 4:
                UI.listar_clientes()
            if op == 5:
                UI.sociedade()

    @classmethod
    def nova_empresa(cls):
        nome = input("Informe o nome da empresa: ")
        cls.empresa = Empresa(nome)

    @classmethod
    def mostrar_empresa(cls):
        print(cls.empresa)

    @classmethod
    def inserir_cliente(cls):
        nome = input("Informe o nome: ")
        cpf = input("Informe o cpf: ")
        limite = float(input("Infome o limite: "))
        cliente = Cliente(nome, cpf, limite)
        cls.empresa.inserir(cliente)

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.empresa.listar():
            print(cliente)

    @classmethod
    def sociedade(cls):
        clientes = cls.empresa.listar()
        print("Lista de clientes")
        for i, cliente in enumerate(clientes):
            print(f"{i}: {cliente}")
        x = int(input("Informe o numero do 1º cliente: "))
        y = int(input("Informe o numero do 2º cliente: "))
        clientes[x].set_socio(clientes[y])

UI.main()