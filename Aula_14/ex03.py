try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
except Exception as erro: # vai pegar qualquer erro que aconteca (mas consegue acessar o objeto de erro)
    print(type(erro))
    print(erro)