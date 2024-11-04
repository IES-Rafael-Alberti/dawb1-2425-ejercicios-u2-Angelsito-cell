
def pedir_nivel(): 
        n = float(input('Introduzca su puntuación: '))
        return n
 
def analizar_nivel(nv):


   if nv == 0.0:
       return f"Inaceptable"
   if nv == 0.4:
       return f"Aceptable"
   if nv >= 0.6:
       return f"Meteorito"
   
def analizar_pago( n): 

    pago_segun_niv = 2400*(n)
    pago = 2400*pago_segun_niv

def main(): 
    
   niv = pedir_nivel()
   p = analizar_pago()
   while analizar_nivel(niv) != None:
        print(f'Tu puntuación ha sido de {niv} y tienes una calificación de {analizar_nivel(niv)}. Tu pago es de {p}')
   else: 
       print("Esa calificación no es válida")
    
if __name__ == "__main__": 
    main()