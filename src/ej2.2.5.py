def inversion():
    num = None
    while num == None:
        num = int(input('Cantidad a invertir: '))
    return num

def interes_anual():
    num = None
    while num == None:
        num = int(input('Interés anual: '))
    return num

def años():
    num = None
    while num == None:
        num = int(input("Introduzca los años de inversión: "))
    return num

def calcular_intereses(cantidad, interes):

    cantidad *= interes / 100
    return cantidad
    

def main():
    cantidad = inversion()
    interes = interes_anual()
    a = años()

    total = 0
    for i in range(0, a):
        t1 = calcular_intereses(cantidad, interes)
        total += t1
        print(total)


if __name__ == '__main__':
    main()