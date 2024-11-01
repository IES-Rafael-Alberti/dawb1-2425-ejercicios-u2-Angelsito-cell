def mostrar_mayor_o_menor(edad: int):
    edad = int()
    if edad <18:
        print(f"Eres menor de edad")
    else: 
        print(f"Eres mayor de edad")
        return edad

def main(): 
    edad = int(input("Introduce tu edad: "))
    mostrar_mayor_o_menor(edad)


if __name__ == "__main__": 
    main()