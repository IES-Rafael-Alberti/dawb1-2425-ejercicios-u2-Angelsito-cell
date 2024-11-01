def pedir_num():
    try:
        num = int(input('Introduce un número: '))

    except ValueError:
        num = f'\n**ERROR**\n El valor introducido solo puede ser un número\n **ERROR**\n'
    except:
        num = f'\n**ERROR**\n Error desconocido \n**ERROR**\n'
    return num


def pedir_otro_numero():
    num = None
    while num == None:
        num = int(input("Introduce otro número: "))
    return num

def pedir_num_float():
    num = None
    while num == None:
        num = float(input("Introduce otro número: "))
    return num

def preguntar_edad():
    return int(input("¿Cuántos años tienes?: "))

def pedir_palabra():
    name = False
    while name == False:
        name = input('Introduza una palabra')
    return name
