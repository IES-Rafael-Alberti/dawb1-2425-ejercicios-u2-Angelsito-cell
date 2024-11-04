def preguntar_pizza(): 
 
 pizza = input("¿Quieres una pizza normal, o vegetariana?: ")
 return pizza.title()
 
def n_o_v(pizza):
    if pizza == "Normal":
        x = "Normal"
    else:
        x = "Vegetariana"
    return x
def ingredientes_n(): 

    print("La pizza por defecto lleva: Tomate y Mozarella")
    print("Ahora elige entre estos Ingredientes: ")

    n = input("Pepperoni, Jamón, Salmón\n")
    n = n.title()

    if n == "Pepperoni":
        return "Pepperoni"
    elif n == "Jamón":
        return "Jamón"
    elif n == "Salmón": 
        return "Salmón"

def ingredientes_v(): 


    print("La pizza por defecto lleva: Tomate y Mozarella")
    print("Ahora elige entre estos Ingredientes: ")

    n = input("Tofu, Pimiento\n")
    n = n.title()

    if n == "Tofu":
        return "Tofu"
    elif n == "Pimiento":
        return "Pimiento"
    
def main(): 
    n = preguntar_pizza()
    tipo_pizza = n_o_v(n)

    if tipo_pizza == "Normal":
        x = ingredientes_n()
    elif tipo_pizza == "Vegetariana": 
        x = ingredientes_v()
    
    print(f'El tipo de pizza que has pedido es {tipo_pizza} con los ingredientes Mozarella, Tomate y {x}')

if __name__ == "__main__": 
    main()