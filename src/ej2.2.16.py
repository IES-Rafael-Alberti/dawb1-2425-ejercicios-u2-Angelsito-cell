from lib import solicitar_numero

def mayor_de_dos(num1: int, num2: int) -> int:
    return num1 if num1 > num2 else num2

def es_cero(numero: int) -> bool:
    return numero == 0

def ejecutar():
    numero = solicitar_numero()
    mayor = numero

    while not es_cero(numero):
        mayor = mayor_de_dos(numero, mayor)
        numero = solicitar_numero()

    print(f'El mayor número ingresado fue: {mayor}')

if __name__ == '__main__':
    ejecutar()
