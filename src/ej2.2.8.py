def pedir_num():
    valor = None
    while valor == None:
        try:
            n = int(input("Introduce un número entero: "))
            if n <=0: 
                raise ValueError ("Introduce un número valido:")
            return n 
        except ValueError:
            print("Por favor, introduce un número entero válido.")

def generar_fila(n):
  
  for i in range(1, n, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")


def main():
    n = pedir_num()
    generar_fila(n)

if __name__ == "__main__":
    main()
