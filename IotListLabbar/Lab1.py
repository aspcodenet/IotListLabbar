
lista = []

for i in range(0,4):
    lista.append(int(input(f"Mata in tal {i+1}:")))


largestSoFar = lista[0]
for i in lista:
    if i > largestSoFar:
        largestSoFar = i

print(largestSoFar)
