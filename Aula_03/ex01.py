x = True

if x:
    print("ok")
print(type(x))
x = 1
if x:
    print("ok")
print(type(x))

if 1 == "Teste":
    print("ok")

if "10" > "2":
    print("A")
else:
    print("B")

x = int(input())
print("par" if x % 2 == 0 else "impar")
# std::cout << x % 2 == 0 ? "par" : "impar" << std::endl; <- C++

print("Digite um valor inteiro entre 1 e 12")
x = int(input())

match x:
    case 1: print("janeiro")
    case 2: print("fevereiro")
    case 3: print("marco")
    case 4: print("abril")
    case 5: print("maio")
    case 6: print("junho")
    case 7: print("julho")
    case 8: print("agosto")
    case 9: print("setembro")
    case 10: print("outubro")
    case 11: print("novembro")
    case 12: print("dezembro")
    case _: print("Mes invalido")

