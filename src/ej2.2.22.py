from lib import solicitar_numero

def es_par(numero: int) -> bool:
    return numero % 2 == 0

def descomponer_en_digitos(numero: int) -> list:
    return [int(digito) for digito in str(numero)]

def ejecutar():
    contador_par = 0
    contador_impar = 0
    lista_par = []
    lista_impar = []

    numero = solicitar_numero()
    while numero != 0:
        digitos = descomponer_en_digitos(numero)
        
        for digito in digitos:
            if es_par(digito):
                contador_par += 1
                lista_par.append(digito)
            else:
                contador_impar += 1
                lista_impar.append(digito)

        numero = solicitar_numero()

    print("Dígitos pares:", lista_par)
    print("Dígitos impares:", lista_impar)
    print("Total de dígitos pares:", contador_par)
    print("Total de dígitos impares:", contador_impar)

if __name__ == '__main__':
    ejecutar()
