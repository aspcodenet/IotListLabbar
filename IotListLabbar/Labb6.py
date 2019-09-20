
class Produkt:
    Namn = ""
    Pris = 0.0
    ProduktNummer = 0

inkopsLista = []
antal = int(input("Hur många varor?"))
for i in range(0, antal):
    p = Produkt()
    p.Namn = input("Ange namn:")
    p.Pris = float(input("Ange pris:"))    
    p.ProduktNummer = int(input("Ange produktnummer:"))
    inkopsLista.append(p)

for p in inkopsLista:
    print(f"{p.Namn} {p.Pris} {p.ProduktNummer}")
