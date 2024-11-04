import os

def solicitar_libro():
    libro_total = ''
    contador_lineas = 0

    while True:
        libro = input('Libro: ')
        
        if libro == '*':
            break
        elif libro == '/':
            cantidad_digitos = contar_digitos(libro_total)
            print(f'Línea completa. Aparecen {cantidad_digitos} dígitos numéricos')
            contador_lineas += 1
            libro_total = ''  # Resetea la línea para la próxima entrada
        else:
            libro_total += ' ' + libro

    print(f'Fin. Se leyeron {contador_lineas} líneas completas.')

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def contar_digitos(texto: str) -> int:
    return sum(1 for caracter in texto if caracter.isdigit())

def ejecutar():
    limpiar_pantalla()
    solicitar_libro()

if __name__ == '__main__':
    ejecutar()
