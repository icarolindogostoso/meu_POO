from datetime import datetime, timedelta
import math

a = datetime(2023, 6 ,1)
b = datetime(2023, 6, 1, 9, 30, 15)

c = datetime.now()
d = datetime.today()

print(a, type(a))
print(b, type(b))

print(c)
print(d)

print(math.sqrt(16))
#modulo.classe.metodo()


#metodos da classe:
f = datetime.strptime("23/06/2023 09:30", "%d/%m/%Y %H:%M")
g = datetime.strptime(input("Informe uma data: "), "%d/%m/%Y")

print(f)
print(g)

#metodos da instancia:
# g.day = 9
print(g.day)
print(g.month)
print(g.year)
print(g.date())
print(g.time())
print(g.weekday())
print(g.strftime("%d/%m/%Y %H:%M"))
print(g.strftime("%A, %d/%B/%Y"))
