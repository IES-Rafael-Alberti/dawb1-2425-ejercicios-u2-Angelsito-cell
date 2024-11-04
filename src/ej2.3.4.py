def solicitar_numero() -> int:
    while True:
        try:
            num = int(input('Introduzca un número: '))
            return num 
        except ValueError:
            print('\n**ERROR**\nLa entrada no es correcta. Por favor, introduzca un número entero.')

def ejecutar():
    num = solicitar_numero()
    print(f'Número ingresado: {num}')  # Muestra el número ingresado

if __name__ == '__main__':
    ejecutar()
