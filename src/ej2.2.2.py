from lib import preguntar_edad

def buc(edad: int):
    for i in range(1,edad+1):
        print(i)

def main():
    edad = preguntar_edad()
    buc(edad)

if __name__ == '__main__':
    main()