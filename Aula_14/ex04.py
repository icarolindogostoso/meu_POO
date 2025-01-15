try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
except ValueError as erro:
    print("Erro de valor")
# except ZeroDivisionError as erro: -> se esse erro nao for destruido e o codigo notar a existencia dele, o codigo vai parar de rodar quando terminar o tratamento
#    print("Erro de divisão por zero")
finally:
    print("ok")
print("fim")