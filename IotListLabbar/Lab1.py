
lista = []

for i in range(0,4):
    lista.append(int(input(f"Mata in tal {i+1}:")))

largest = lista[0]
for i in range(1,4):
    if lista[i] > largest:
        largest = lista[i]

print(largest)
