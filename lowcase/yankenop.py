import random as RA

def mostrar_resultado(jugador, computadora):
    if jugador == computadora:
        return "¡Es un empate!"
    elif (jugador == "PI" and computadora == "TI") or (jugador == "PA" and computadora == "PI") or (jugador == "TI" and computadora == "PA"):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

print('Bienvenido al sistema de Piedra, Papel o Tijeras!')
print('Opciones:')
print('PI = Piedra')
print('PA = Papel')
print('TI = Tijeras')

letra = input('Ingresa tu opción (PI, PA, TI): ').strip().upper()

if letra not in ["PI", "PA", "TI"]:
    print("Opción invalida, vuelva a ejecutar el programa.")
else:
    opciones = ["PI", "PA", "TI"]
    computadora = RA.choice(opciones)

    if letra == "PI":
        print("Elegiste Piedra.")
    elif letra == "PA":
        print("Elegiste Papel.")
    else:
        print("Elegiste Tijeras.")

    if computadora == "PI":
        print("La computadora eligió Piedra.")
    elif computadora == "PA":
        print("La computadora eligió Papel.")
    else:
        print("La computadora eligió Tijeras.")

    resultado = mostrar_resultado(letra, computadora)
    print(resultado)