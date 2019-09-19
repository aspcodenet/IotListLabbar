
class Person:
    Namn = ""
    GatuAdress = ""
    PostNummer = ""
    Postort = ""

lista = []

while True:
    p = Person()
    p.Namn = input("Ange namn:")
    p.GatuAdress = input("Ange gatuadress:")    
    p.PostNummer = input("Ange postnummer:")    
    p.PostOrt = input("Ange postort:")    
    lista.append(p)

    if input("Fler inmatningar? J/N").upper() != "J":
        break
    
for p in lista:
    print(f"{p.Namn} {p.GatuAdress} {p.PostNummer} {p.Postort}")
