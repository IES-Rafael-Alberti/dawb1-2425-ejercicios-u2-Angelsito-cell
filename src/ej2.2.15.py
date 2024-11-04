from lib import solicitar_numero

def es_cero(numero: int) -> bool:
    return numero == 0

def es_negativo(numero: int) -> bool:
    return numero < 0

def ejecutar():
    numero = solicitar_numero()
    suma_total = 0

    while not es_cero(numero):
        if not es_negativo(numero):
            suma_total += numero
        else:
            print('El número introducido no puede ser negativo')
        numero = solicitar_numero()

    print(f'La suma de todos los números introducidos es: {suma_total}')

if __name__ == '__main__':
    ejecutar()
