def comprobar_divisor(): 
    while True: 
        try:   
            num2 = int(input("Introduce un divisor (no puede ser 0): "))

            if num2 == 0: 
                raise ValueError("**ERROR** El divisor no puede ser 0")
            
            return num2
        except ValueError:
            print("Por favor, introduce un divisor válido (pista: Mayor que 0).")

def div(): 
    num1 = int(input("Introduzca un dividendo: "))
    num2 = comprobar_divisor()  # Llama a la función para pedir y validar el divisor

    resultado = num1 / num2
    print(f"El resultado es: {resultado}")
    return resultado

def main(): 
    div()  # Llama a la función `div` que realiza toda la operación

if __name__ == "__main__": 
    main()

