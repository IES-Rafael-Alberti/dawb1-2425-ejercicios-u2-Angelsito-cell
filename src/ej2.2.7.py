
from lib import pedir_num

def calcular_tabla(n):

    for i in range (11):
        total = n * i
    return total

def main():
    n = pedir_num()
    for i in range(n+1):
        total = calcular_tabla(i)
        print(f'{n} x {i} = {total}')

if __name__ == '__main__':
    main()