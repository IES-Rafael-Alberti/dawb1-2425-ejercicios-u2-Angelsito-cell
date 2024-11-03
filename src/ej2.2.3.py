from lib import pedir_num

def primos(num: int):
    serie = ' '
    for i in range(1, num + 1, 2):
        i = str(i)
        serie += i + ', '
    serie = serie.rstrip(', ')
    return serie

def main():
    n = pedir_num()
    print(f'{primos(n)}')

if __name__ == '__main__':
    main()