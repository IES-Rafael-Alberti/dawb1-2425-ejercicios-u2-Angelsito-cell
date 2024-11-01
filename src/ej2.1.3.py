
def comprobar_divisor(): 
    while True: 
     try:   
        num2 = int(input("Introduce un divisor: "))
        if num2==0: 
            raise ValueError ("**ERROR** El divisor no puede ser 0")
        return num2
     except ValueError:
        print("Por favor, introduce un divisor válido (pista: Mayor que 0).")

def div(num1, num2):
    
    while comprobar_divisor():
        num1 =  int(input("Introduzca un dividendo: "))
        div = num1/num2()
        print(f"El resultado es: {div}")
    return div

def main(): 
    div()

if __name__ == "__main__": 
    main()