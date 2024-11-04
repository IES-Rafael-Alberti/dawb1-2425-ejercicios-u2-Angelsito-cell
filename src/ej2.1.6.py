def preguntar_sex():
    n = input ("Introduzca su sexo (M o F): ")
    return n.title()

def preguntar_nom(): 
    n = input("Introduzca su nombre: ")
    return n.title()

def comprobar_grupo(a, b): 

   if a == 'Hombre':
        if 'a' <= b[0] <= 'm':
            return f'Estás en el grupo B'
        else:
            return f'Estás en el grupo A'
   else:
        if  'n' <= b[0] <= 'z':
            return f'Estás en el grupo A'
        else:
            return f'Estás en el grupo B'

def main(): 
    
    a = preguntar_nom()
    b = preguntar_sex()

    print(comprobar_grupo(a,b))

if __name__ == "__main__": 
    main()