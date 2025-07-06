dinero = float(input("¿Cuanto dinero tiene en nuestro banco? : "))

def formato():
    print(f"""
=====================================================================
        Welcome to ChavinStudios Bank's
    
        ¿What do u wanna do?
      
        1 ) Deposit
        2 ) Withdraw
        3 ) Exit
      
        Remember if u have problems, you can tell us on own email!
        info@chavinstudios.com
=====================================================================
      """)

formato()

select = 0

while select != 3:
    
    select = int(input())
    
    if select == 1:
        print("")
        cantidad = int(input("| ✅ | ¿Cual es la cantidad que desea depositar? : "))
        print("🎈 | Listo, ahora su dinero es de ",(dinero + cantidad)," soles")
        formato()
    if select == 2:
        print("")
        cantidad = int(input("| ✅ | ¿Cual es la cantidad que desea quitar? : "))
        print("🎈 | Listo, ahora su dinero es de ",(dinero - cantidad)," soles")
        formato()
        
    if select == 3:
        print("")
        cantidad = print("| ✅ | ¡Gracias por contar con ChavinStudios! ")
        exit
        
        
        