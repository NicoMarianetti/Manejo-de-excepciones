'''

    El siguiente código pide el ingreso de un usuario pero se rompe cuando el ingreso no puede castearse a entero, utilizar un bloque try-catch
    para que no termine la ejecución del programa e indicar el usuario su error.

'''

def main():
    ingreso = int(input("Ingrese un número: "))

    print("El número ingresado es: ", ingreso)

main()