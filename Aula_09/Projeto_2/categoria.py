import json

class Categoria:
    def __init__ (self, id, d):
        self.setId(id)
        self.setDescricao(d)

    def setId (self, id):
        if id > 0:
            self.__id = id
        else:
            raise ValueError ("Id invalido")
        
    def setDescricao(self, d):
        if len(d) > 0:
            self.__descricao = d
        else:
            raise ValueError ("Descicao invalida")
        
    def getId (self):
        return self.__id
        
    def __str__ (self):
        return f"{self.__id} - {self.__descricao}"
    
class Categorias:
    objetos = []

    @classmethod
    def inserir (cls, obj):
        cls.objetos.append(obj)

    @classmethod
    def listar (cls):
        return cls.objetos
    
    @classmethod
    def listarId (cls, id):
        for categoria in cls.objetos:
            if categoria.getId() == id:
                return categoria
            
    @classmethod
    def atualizar (cls, obj):
        for i, categoria in enumerate(cls.objetos):
            if categoria.getId() == obj.getId():
                cls.objetos[i] = obj

    @classmethod
    def excluir (cls, obj):
        for i, categoria in enumerate(cls.objetos):
            if categoria.getId() == obj.getId():
                del cls.objetos[i]

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("Aula_09/Projeto_2/categorias.json", mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Categoria(obj["id"], obj["d"])
                cls.objetos.append(c)

    @classmethod
    def salvar(cls):
        with open("Aula_09/Projeto_2/categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)