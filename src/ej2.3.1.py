from lib import ingresar_edad

def mostrar_anios_cumplidos(edad: int) -> None:
    for anio in range(1, edad + 1):
        print(anio, end=' ')
    print()

def validar_edad(edad: int) -> bool:
    if edad < 1:
        raise ValueError('La edad introducida no debe ser menor a 1 o negativa.')
    elif edad > 125:
        raise ValueError('La edad introducida no debe ser mayor a 125.')
    return True

def ejecutar():
    try:
        edad = ingresar_edad()
        if validar_edad(edad):
            mostrar_anios_cumplidos(edad)
    except ValueError as e:
        print(f"**ERROR** {e}")

if __name__ == '__main__':
    ejecutar()
