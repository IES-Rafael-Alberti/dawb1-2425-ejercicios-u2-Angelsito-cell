def par_impar(div): 
 
 num = int(input("Introduce un número: "))

 if num%2 == 0: 
    print("Tu número es par")
 else: 
    print("Tu número es impar")

    return num

def main(): 
    num = ""
    par_impar(num)


if __name__ == "__main__": 
    main()