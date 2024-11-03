from lib import pedir_numero

def bucle(num: int):
    serie = ''
    for i in reversed(range(0, num + 1)):
        i = str(i)
        serie += i + ', '
    serie = serie.rstrip(', ')
    return serie

def main():
    num = pedir_numero()
    print(bucle(num))

if __name__ == '__main__':
    main()