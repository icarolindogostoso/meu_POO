def aprovado(nota1, nota2):
    media = (nota1 + nota2)/2
    if media < 60:
        return False
    return True

nota1 = int(input())
nota2 = int(input())
passou = aprovado(nota1,nota2)
if passou:
    print("Aprovado!")
else:
    print("Recuperação!")