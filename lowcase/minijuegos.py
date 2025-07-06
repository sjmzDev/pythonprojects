# Version 1.0
# Code developed by sjmz

def yankenpo():
        print('Bienvenido al juego de Piedra, Papel y Tijera!')
        elección = input('Cual desea elegir? [PI(Piedra), PA(Papel), TI(Tijera)] : ')
        
        if elección == "PI":
                print(f'Usted escogio {elección}')
        elif elección == "PA":
                print(f'Usted escogio {elección}')
        elif elección == "TI":
                print(f'Usted escogio {elección}')

nombre = input('Introduzca su nombre: ')

print(f"Bienvenido {nombre}, que le gustaría hacer el día de hoy?")
primer_eleccion = print("""
===========================================
             ¡MiniJuegos!
        1) Piedra, Papel o Tijera
        2) Soon..
        3) Soon..

===========================================      
""")

primer_eleccion = 0

while primer_eleccion != 3:
     
        primer_eleccion = input('')
     
        if primer_eleccion == 1:
                yankenpo()
        elif primer_eleccion == 2:
                print('| 🟥 |No esta disponible por el momento.')
        elif primer_eleccion == 3:
                print('| 🟥 |No esta disponible por el momento.')
        else:
                print('Error al momento de insertar.')
                
