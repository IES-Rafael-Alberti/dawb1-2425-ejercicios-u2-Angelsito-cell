def comprobar_tributo(): 
 edad = int(input("Introduce tu edad, usuario: "))
 ing =  int (input("Introduce tus ingresus mensuales, usuario: "))
 
 if edad < 16 or ing < 1000: 
    print("Usted no ha de tributar")
 else: 
    print("Usted ya ha de tributar")
 return edad and ing
 
def main(): 
    tributo = ""
    comprobar_tributo()

if __name__ == "__main__": 
    main()