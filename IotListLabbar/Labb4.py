
lista = []

num = int(input("Hur många mätningar?"))
for i in range(0,num):
    lista.append(float(input(f"Ange temperatur för mätning {i+1}:")))


for i in lista:
    print(i)

max=lista[0]
sum=0
for i in lista:
    if i > max: 
        max = i
    sum = sum + i

print(f"max {max} avg {sum/len(lista)}")


