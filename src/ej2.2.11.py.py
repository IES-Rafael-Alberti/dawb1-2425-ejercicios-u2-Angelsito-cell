
def pedir_frase():
    return input('Introduzca una frase: ')

def separar_frase(frase: str):
    palabra = list(frase)
    return palabra

def main():
    n = pedir_frase()
    print(f'{separar_frase(n)}')

if __name__ == '__main__':
    main()