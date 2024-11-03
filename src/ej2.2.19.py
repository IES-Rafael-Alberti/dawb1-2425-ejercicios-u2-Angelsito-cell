import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_seleccion():
    try:
        return int(input('\nElige una opción:\n 1.- Comenzar programa\n 2.- Imprimir listado\n 3.- Finalizar programa\n\n> '))
    except ValueError:
        print("**ERROR** Debes ingresar un número.")
        return obtener_seleccion()

def menu():
    while True:
        seleccion = obtener_seleccion()
        
        if seleccion == 1:
            print('Has seleccionado la opción uno.')
        elif seleccion == 2:
            print('Has seleccionado la opción dos.')
        elif seleccion == 3:
            print('\nHasta luego.')
            time.sleep(2)
            limpiar_pantalla()
            break
        else:
            print('**ERROR** La selección no está reconocida. Elige una opción válida.')

def ejecutar():
    menu()

if __name__ == '__main__':
    ejecutar()
