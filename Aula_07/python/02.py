class Playlist:
    def __init__ (self, nome, descricao):
        self.__setNome(nome)
        self.__setDescricao(descricao)
        self.__musicas = []

    def __setNome (self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError ("Sem nome")

    def __setDescricao (self, descricao):
        if len(descricao) > 0:
            self.__descricao = descricao
        else:
            raise ValueError ("Sem descricao")

    def inserir (self, musica):
        self.__musicas.append(musica)

    def listar (self):
        return self.__musicas
    
    def __str__ (self):
        return f"Playlist: {self.__nome}\nDescricao: {self.__descricao}"


class Musica:
    def __init__ (self, titulo, artista, album):
        self.__setTitulo(titulo)
        self.__setArtista(artista)
        self.__setAlbum(album)

    def __setTitulo (self, titulo): 
        if len(titulo) > 0:
            self.__titulo = titulo
        else:
            raise ValueError ("Sem titulo")
        
    def __setArtista (self, artista): 
        if len(artista) > 0:
            self.__artista = artista
        else:
            raise ValueError ("Sem artista")
        
    def __setAlbum (self, album):
        if len(album) > 0:
            self.__album = album
        else:
            raise ValueError ("Sem descricao")
    
    def __str__ (self):
        return f"Musica: {self.__titulo} - Artista: {self.__artista} - Album: {self.__album}"


class UI:
    @staticmethod
    def menu():
        print("1 - Nova playlist, 2 - Inserir musica na playlist, 3 - Mostrar playlist, 9 - Fim")
        return int(input("Informe uma opcao: "))
    
    @staticmethod
    def main():
        op = 0
        playlist = None

        while op != 9:
            op = UI.menu()
            if op == 1:
                playlist = UI.novaPlaylist()
            if op == 2:
                if playlist == None:
                    print("Nenhuma playlist criada")
                    print("\n")
                else:
                    UI.inserirMusica(playlist)
            if op == 3:
                if playlist == None:
                    print("Nenhuma playlist criada")
                    print("\n")
                else:
                    UI.mostrarPlaylist(playlist)

    @staticmethod    
    def novaPlaylist ():
        nome = input("Insira o nome da playlist: ")
        descricao = input("Insira uma descricao para a playlist: ")
        print("\n")
        x = Playlist(nome, descricao)
        return x
    
    @staticmethod
    def inserirMusica (playlist):
        titulo = input("Insira o titulo da musica: ")
        artista = input("Insira o artista da musica: ")
        album = input("Insira o album da musica: ")
        print("\n")
        musica = Musica(titulo, artista, album)
        playlist.inserir(musica)

    @staticmethod
    def mostrarPlaylist (playlist):
        print(playlist)
        for musica in playlist.listar():
            print(musica)
            print("\n")

UI.main()