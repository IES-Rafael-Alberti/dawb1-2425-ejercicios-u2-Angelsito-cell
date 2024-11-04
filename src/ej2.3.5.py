def solicitar_contraseña() -> str:
    return input('Introduzca su contraseña: ')

def verificar_contraseña(contra: str) -> None:
   try:
        if contra != 'contraseña':
            raise NameError('Incorrect Password!!')
        else:
            print('La contraseña es correcta')

   except NameError as e:
        print(e)
        
def ejecutar():
    contra = solicitar_contraseña()
    verificar_contraseña(contra)

if __name__ == '__main__':
    ejecutar()
