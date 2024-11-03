def solicitar_monto_total():
    monto_total = 0
    
    while True:
        try:
            monto = int(input('Introduce el monto de la empresa (0 para finalizar): '))
        except ValueError:
            print("**ERROR** Solo se permite ingresar un número entero")
            continue
        
        if monto == 0:
            break
        elif monto < 0:
            print('**ERROR** El monto ingresado no puede ser negativo')
        else:
            monto_total += monto
            
    return monto_total

def aplica_descuento(monto: int) -> bool:
    return monto > 1000

def ejecutar():
    monto = solicitar_monto_total()

    if aplica_descuento(monto):
        monto -= monto * 0.10 

    print(f'El total a pagar sería de {monto}€')

if __name__ == '__main__':
    ejecutar()
