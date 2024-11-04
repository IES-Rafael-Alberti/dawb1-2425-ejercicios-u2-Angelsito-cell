from lib import solicitar_numero

def es_negativo_restringido(numero: int) -> bool:
    if numero == -1:
        return True
    elif numero < -1:
        raise ValueError('**ERROR** No puedes introducir un valor menor a -1')
    return False

def ejecutar():
    numero = solicitar_numero()
    suma_total = 0

    while not es_negativo_restringido(numero):
        suma_total += numero
        numero = solicitar_numero()

    print(f'La suma de los números introducidos es: {suma_total}')

if __name__ == '__main__':
    ejecutar()
