a = int(input())

if a == 1:
    primeiro_valor = 0
    print(primeiro_valor)
else:
    primeiro_valor = 0
    segundo_valor = 1
    print(primeiro_valor,segundo_valor,end=' ')
    for i in range(a-2):
        valor = primeiro_valor + segundo_valor
        print(valor, end=' ')
        primeiro_valor = segundo_valor
        segundo_valor = valor
