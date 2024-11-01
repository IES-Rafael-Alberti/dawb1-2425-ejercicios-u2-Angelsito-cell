def renta():
  
  return int(input("Introduzca su renta anual: "))

def comprobar_renta(): 

 r = renta()
 if r < 10000:
        print('Debe pagar un 5%')
 if 10000 <= r < 20000:
        print('Debe pagar un 15%')
 if 20000 <= r < 35000:
        print('Debes pagar un 20%')
 if 35000 <= r < 60000:
        print('Debes pagar un 30%')
 if 60000 <= r:
        print('Debes pagar un 45%')

def main(): 

 comprobar_renta()


if __name__ == "__main__": 
    main()