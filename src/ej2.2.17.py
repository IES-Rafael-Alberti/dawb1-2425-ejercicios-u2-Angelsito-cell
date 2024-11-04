from lib import solicitar_numero

def descomponer_en_digitos(numero: int) -> list:
    return [int(digito) for digito in str(numero)]

def sumar_digitos(digitos: list) -> int:
    return sum(digitos)

def ejecutar():
    numero = solicitar_numero()
    digitos = descomponer_en_digitos(numero)
    suma_total = sumar_digitos(digitos)
    print(f'La suma de los dígitos que componen el número es: {suma_total}')

if __name__ == '__main__':
    ejecutar()
