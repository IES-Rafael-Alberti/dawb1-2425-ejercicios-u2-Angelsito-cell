import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def solicitar_frase() -> str:
    return input('Introduzca una frase: ').strip()

def dividir_palabras(frase: str) -> list:
    return frase.split()

def obtener_palabra_mas_larga(palabras: list) -> tuple:
    palabra_mas_larga = max(palabras, key=len) if palabras else ""
    return len(palabra_mas_larga), palabra_mas_larga

def ejecutar():
    limpiar_pantalla()
    frase = solicitar_frase()

    palabras = dividir_palabras(frase)
    mayor_longitud, palabra_mas_larga = obtener_palabra_mas_larga(palabras)

    print(f'La palabra más larga es "{palabra_mas_larga}" con {mayor_longitud} caracteres.')
    print(f'Número total de palabras: {len(palabras)}')

if __name__ == '__main__':
    ejecutar()

        