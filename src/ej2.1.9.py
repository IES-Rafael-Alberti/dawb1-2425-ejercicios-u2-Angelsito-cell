def pedir_entrada(): 
 return int(input("Introduzca su edad, usuario: "))
def analizar_edad():
   
   edad = pedir_entrada()

   if edad < 4: 
      print("Tu entrada es gratuita!")
   if 4<= edad < 18: 
      print("Tu entrada cuesta 5 euros")
   if 18 <= edad: 
      print("Tu entrada cuesta 10 euros")

def main(): 
    
    analizar_edad()
if __name__ == "__main__": 
    main()