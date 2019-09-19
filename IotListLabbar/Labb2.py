
lista = []

antal = int(input("Hur många tal?"))
for i in range(0,antal):
    lista.append(int(input(f"Mata in tal {i+1}:")))

largest = lista[0]
for i in range(1,len(lista)):
    if lista[i] > largest:
        largest = lista[i]

print(largest)
