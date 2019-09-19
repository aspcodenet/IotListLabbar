def func_a():
    listaVarden = []
    listaDatum = []

    num = int(input("Hur många mätningar?"))
    for i in range(0,num):
        listaVarden.append(float(input(f"Ange temperatur för mätning {i+1}:")))
        listaDatum.append(input("Ange datum för mätning {i+1}:"))


    for i in range(0,listaVarden):
        print(f"{listaDatum[i]} {listaVarden[i]}")

    maxIndex = 0
    minIndex = 0
    for i in range(0,listaVarden):
        if listaVarden[i] > listaVarden[maxIndex]: 
            maxIndex = i
        if listaVarden[i] < listaVarden[minIndex]: 
            minIndex = i

    print(f"max {listaVarden[maxIndex]}  uppmättes {listaDatum[maxIndex]}")
    print(f"min {listaVarden[minIndex]}  uppmättes {listaDatum[minIndex]}")


class TemperatureMeasurement:
    Datum = ""
    Varde  = 0.0

def func_b():
    lista = []
    num = int(input("Hur många mätningar?"))
    for i in range(0,num):
        varde = float(input(f"Ange temperatur för mätning {i+1}:"))
        datum = input("Ange datum för mätning {i+1}:")
        m = TemperatureMeasurement()
        m.Datum = datum
        m.Varde = varde
        lista.append(m)


    for measure in lista:
        print(f"{measure.Datum} {measure.Varde}")

    maxMeasure = lista[0]
    minMeasure = lista[0]
    for measure in lista:
        if measure.Varde > maxMeasure.Varde: 
            maxMeasure = measure
        if measure.Varde < minMeasure.Varde: 
            minMeasure = measure

    print(f"max {maxMeasure.Datum}  uppmättes {maxMeasure.Varde}")
    print(f"min {minMeasure.Datum}  uppmättes {minMeasure.Varde}")



