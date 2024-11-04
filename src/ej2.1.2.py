def variable():
    c = "aitortilla"
    return c
def comprobar_contraseña(con): 
 while True:
    intento = input("Introduzca la contraseña: ")
    if intento != con: 
        print("La contraseña no es correcta, introdúcela de nuevo: ")
    else: 
       print("La contraseña es correcta")
       break

def main(): 
    con = variable()
    comprobar_contraseña(con)


if __name__ == "__main__": 
    main()