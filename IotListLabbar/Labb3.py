
lista = [321,3212,312,3,66]

num = 0
for i in lista:
    if i % 2 == 1:
        lista[num] = 0
    num = num + 1


for i in lista:
    print(i)
