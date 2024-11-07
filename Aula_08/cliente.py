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