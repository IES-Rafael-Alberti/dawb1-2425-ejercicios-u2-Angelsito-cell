from lib import solicitar_numero

def es_cero(numero) -> bool:
    return numero == 0

def ejecutar():
    numero = solicitar_numero()
    suma_total = 0

    while not es_cero(numero):
        suma_total += numero
        numero = solicitar_numero()


    print(f'La suma total de los números ingresados es: {suma_total}')

if __name__ == '__main__':
    ejecutar()
