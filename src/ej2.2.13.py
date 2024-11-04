import os

def solicitar_palabra():
    return input('Introduce una palabra (escribe "salir" para finalizar): ')

def verificar_salida(texto: str) -> bool:
    return texto.lower() == 'salir'

def ejecutar_programa():
    os.system('cls' if os.name == 'nt' else 'clear')
    texto = solicitar_palabra()
    while not verificar_salida(texto):
        print(f'> {texto}')
        texto = solicitar_palabra()

if __name__ == '__main__':
    ejecutar_programa()
