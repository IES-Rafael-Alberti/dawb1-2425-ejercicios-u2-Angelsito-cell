
def preguntar_frase():
    frase = input('Introduzca una frase: ')
    return frase.lower()

def preguntar_letra():
    letra = input('Introduzca una letra: ')
    return letra.lower()

def contar_letras(frase, letra):
    letras = frase.count(letra)
    return letras

def encontrar_letra(frase, letra):
    salida = ''
    for i in range(0, len(frase)):
        if frase[i] == letra:
            salida += str(i + 1) + ' '
    return salida

def main():
    frase = preguntar_frase()
    letra = preguntar_letra()
    total = contar_letras(frase, letra)

    if total == 0:
        print('No se encontro el caracter dentro de la frase')
    else: 
        pos = encontrar_letra(frase, letra)
        print(f'En la frase hay {total} {letra} y están en la posición {pos}')


if __name__ == '__main__':
    main()