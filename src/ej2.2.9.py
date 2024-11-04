def int_contraseña():
    return input('Introduzca la contraseña: ')
def comprobar_contraseña(contraseña):
    comprobacion = False
    while comprobacion == False:
        contraseña = input('Contraseña incorrecta\n Introduzca una contraseña correcta (pista: igual que la de tu cuenta de iesrafaelalberti): ')
        if contraseña == 'aitortilla':
            comprobacion = True
    return comprobacion
def main():
    contraseña = int_contraseña()
    if comprobar_contraseña(contraseña) == True:
        print(f'Contraseña correcta, puede pasar')
if __name__ == '__main__':
    main()
