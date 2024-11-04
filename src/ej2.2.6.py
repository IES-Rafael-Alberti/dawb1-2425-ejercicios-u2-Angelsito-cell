
from lib import pedir_num

def triangulo(num):
    serie = ''
    for i in range(num):
        serie = serie + '*'
    return serie

def main():
    num = pedir_num()
    for i in range(1, num + 1):
        print(triangulo(i))

if __name__ == '__main__':
    main()