def solicitar_frase(): 
    frase = input('Por favor, introduzca una frase: ')
    return frase.lower()

def solicitar_letra():
    letra = input('Por favor, introduzca una letra: ')
    return letra.lower()

def contar_ocurrencias(frase, letra):
    return frase.count(letra)

def ejecutar():
    frase = solicitar_frase()
    letra = solicitar_letra()

    cantidad = contar_ocurrencias(frase, letra)
    print(f'La letra "{letra}" aparece {cantidad} veces en la frase.')

if __name__ == '__main__':
    ejecutar()
