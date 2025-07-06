# Code Developed by sjmz or sebastian

nombre = "sebas"

vendedores = ["Andrea", "Alex", "Pedro", "Juan", "Cesar", "Roger"]
ventas = [15, 16, 1, 0, 4, 21]

cuota_ventas = 6

comisionAuto = 1000

def obtener_total_ventas(ventas):
    return sum(ventas)

def porcentaje_superaron_cuota(ventas, cuota_ventas, vendedores):
    vendedores_superaron = []

    for i in range(len(ventas)):
        if ventas[i] > cuota_ventas:
            vendedores_superaron.append(vendedores[i])
    
    porcentaje = (len(vendedores_superaron) / len(vendedores)) * 100
    return porcentaje, vendedores_superaron

def calcular_comisiones(ventas, comision_por_auto):
    total_ventas = sum(ventas)
    return total_ventas * comision_por_auto

total_ventas = obtener_total_ventas(ventas)
porcentaje, vendedores_superaron = porcentaje_superaron_cuota(ventas, cuota_ventas, vendedores)
comisiones_totales = calcular_comisiones(ventas, comisionAuto)

print(f"Bienvenidos a la practica 08, hecha por {nombre}")
print("")
print("Estos son los resultados :")
print("")
print(f"Total de unidades vendidas: {total_ventas}")
print("")
print(f"Porcentaje de vendedores que superaron la cuota de venta: {porcentaje:.2f}%")
print("")
print(f"Vendedores que superaron la cuota de venta: '{vendedores_superaron}")
print("")
print(f"Total de comisiones a pagar: {comisiones_totales} soles")