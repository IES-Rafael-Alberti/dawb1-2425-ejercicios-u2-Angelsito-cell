from lib import solicitar_numero

def contar_divisores(numero):
    divisores_contados = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores_contados += 1
    return divisores_contados

def main():
    numero = solicitar_numero()

    if isinstance(numero, int):
        if contar_divisores(numero) <= 1:
            print(f'El número {numero} es un número primo')
        else:
            print(f'El número {numero} no es un número primo')
    else:
        print(numero)

if __name__ == '__main__':
    main()

