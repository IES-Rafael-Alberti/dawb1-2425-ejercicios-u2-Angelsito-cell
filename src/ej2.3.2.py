def solicitar_numero() -> int:
    while True:
        try:
            num = int(input('Introduzca un número (mayor o igual a 1): '))
            if num < 1:
                raise ValueError('El número debe ser igual o mayor a uno.')
            return num
        except ValueError as e:
            print(f'\n**ERROR**\n{e}')

def generar_serie(num: int) -> str:
    serie = ', '.join(str(i) for i in range(1, num + 1, 2)) + '.'
    return serie

def ejecutar():
    num = solicitar_numero()
    cadena = generar_serie(num)
    print(f'Los años cumplidos: {cadena}')

if __name__ == '__main__':
    ejecutar()
