def solicitar_numero():
    try:
        numero = int(input('Por favor, introduce un número: '))
    except ValueError:
        numero = '\n**ERROR**\n Solo se permite ingresar un número entero\n **ERROR**\n'
    except:
        numero = '\n**ERROR**\n No se pudo encontrar el recurso (404 Not Found)\n **ERROR**\n'
    return numero

def solicitar_otro_numero():
    otro_numero = None
    while otro_numero is None:
        otro_numero = int(input("Introduce otro número por favor: "))
    return otro_numero

def solicitar_numero_decimal():
    decimal = None
    while decimal is None:
        decimal = float(input("Introduce un número decimal: "))
    return decimal

def ingresar_edad():
    return int(input("¿Cuál es tu edad? "))

def ingresar_palabra():
    palabra = None
    while not palabra:
        palabra = input("Por favor, introduce una palabra: ")
    return palabra
