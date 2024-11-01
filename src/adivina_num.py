import random

# Variables iniciales
numero_oculto = 0  # Número oculto configurable por el usuario
intentos_maximos = 5

# Función para mostrar el menú principal
def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Jugar Juego")
    print("2. Configurar Juego")
    print("3. Mostrar Configuración")
    print("4. Salir")

# Función para configurar el número oculto
def configurar_juego():
    global numero_oculto
    while True:
        entrada = input("\nIngrese el número oculto (o escriba 'Exit' para salir): ")
        if entrada.lower() == "exit":
            break
        try:
            numero_oculto = int(entrada)
            print(f"Número oculto configurado exitosamente a {numero_oculto}")
            break
        except ValueError:
            print("Por favor, introduzca un número válido.")

# Función para mostrar la configuración actual
def mostrar_configuracion():
    print(f"\nEl número oculto es {numero_oculto}")

# Función para jugar el juego
def jugar_juego():
    if numero_oculto == 0:
        print("\nPrimero configure el número oculto en la opción 2 del menú.")
        return
    
    intentos = intentos_maximos
    while intentos > 0:
        try:
            entrada = input(f"\nAdivine el número (o escriba 'Exit' para salir): ")
            if entrada.lower() == "exit":
                break
            
            intento = int(entrada)
            diferencia = abs(numero_oculto - intento)

            if intento == numero_oculto:
                print(f"**CORRECTO** ¡Has ganado! (conseguido en {intentos_maximos - intentos + 1} intentos).")
                break
            elif diferencia > 10:
                pista = "mayor" if intento < numero_oculto else "menor"
                print(f"**FRIO FRIO** El número es {pista} [{intentos - 1} intentos restantes]")
            elif diferencia > 5:
                pista = "mayor" if intento < numero_oculto else "menor"
                print(f"**CALIENTE CALIENTE** El número es {pista} [{intentos - 1} intentos restantes]")
            else:
                pista = "mayor" if intento < numero_oculto else "menor"
                print(f"**TE QUEMAS** El número es {pista} [{intentos - 1} intentos restantes]")
            
            intentos -= 1

            if intentos == 0:
                print(f"Lo siento, has fallado (el número era {numero_oculto}).")

        except ValueError:
            print("Por favor, introduzca un número válido.")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            jugar_juego()
        elif opcion == "2":
            configurar_juego()
        elif opcion == "3":
            mostrar_configuracion()
        elif opcion == "4":
            print("Bye Bye")
            break
        else:
            print("Introduzca una opción válida.")

# Ejecución del programa
if __name__ == "__main__":
    main()
