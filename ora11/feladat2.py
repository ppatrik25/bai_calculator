import random

lista = []
paros = []
paratlan = []
for i in range(100):
    lista.append(random.randint(0, 100))
print(lista)
for elem in lista:
    if elem % 2 == 0:
        paros.append(elem)
    else:
        paratlan.append(elem)
for elem in paros:
    print(elem)
for elem in paratlan:
    print(elem)