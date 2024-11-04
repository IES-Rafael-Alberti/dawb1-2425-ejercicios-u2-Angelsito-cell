def ordenar(a):
    n = len(a)

    for i in range(n):
        ordenado = True
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ordenado = False

        if ordenado:
            break
    return a

def main():
    a = [8, 4, 1, 19, 14]
    print(ordenar(a))

if __name__ == '__main__':
    main()
