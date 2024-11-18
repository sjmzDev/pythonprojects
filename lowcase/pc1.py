# Code Developed by sjmz or sebastian

nombre = "sebas"

comidas = ["Lomo Saltado", "Aji de Gallina", "Papa Rellena", "Seco con Frijoles", "Pollo a la Brasa"]
nacionales = [25000, 18600, 14400, 12000, 30000]
extranjeros = [10000, 5000, 200, 800, 60000]

def calcular_totales(nacionales, extranjeros):
    totales = []
    for i in range(len(nacionales)):
        total = nacionales[i] + extranjeros[i]
        totales.append(total)
    return totales

def calcular_porcentajes(totales):
    total_general = sum(totales)
    porcentajes = [(total / total_general) * 100 for total in totales]
    return porcentajes

def plato_mas_vendido(comidas, totales):
    max_ventas = max(totales)
    indice_max = totales.index(max_ventas)
    return comidas[indice_max]


totales = calcular_totales(nacionales, extranjeros)
porcentajes = calcular_porcentajes(totales)
plato_vendido = plato_mas_vendido(comidas, totales)


print(f"Bienvenidos a la practica 08, hecha por {nombre}")
print("")
print("Estos son los resultados :")
print("")
print("Totales de cada plato (Nacional + Extranjero):")
for i in range(len(comidas)):
    print(f"- {comidas[i]}: - {totales[i]}")

print("Porcentajes de cada plato respecto al total:")
for i in range(len(comidas)):
    print(f"- {comidas[i]}: - {porcentajes[i]:.2f}%") # El .2f significa que le hace un valor de 2  decimales, como que agarra 2 decimales y se redondean

print(f"El plato más vendido es: {plato_vendido}")