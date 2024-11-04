import os
from lib import solicitar_numero

def es_primo(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def verificar_no_negativo(num: int):
    if num < 0:
        raise ValueError('El número introducido no puede ser negativo')

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def ejecutar():
    limpiar_pantalla()
    contador_primos = 0

    num = solicitar_numero()
    verificar_no_negativo(num)

    while num != 0:
        if es_primo(num):
            contador_primos += 1
        num = solicitar_numero()
        verificar_no_negativo(num)    
    
    print(f'Se han ingresado {contador_primos} números primos')

if __name__ == '__main__':
    ejecutar()


