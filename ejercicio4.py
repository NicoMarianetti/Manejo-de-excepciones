'''
    El siguiente código pide al usuario un ingreso de un número y lo utiliza para indexar una lista, pero pueden pasar 2 cosas:
    1- El usuario ingresa un número que no puede ser casteado a entero.
    2- El usuario ingresa un número que no es un índice válido para la lista.

    Utilizar un bloque try-catch para que no termine la ejecución del programa e indicar al usuario cual de los 2 errores cometió.
'''

def main():
    lista = [1, 2, 3, 4, 5]
    ingreso = int(input("Ingrese un número: "))
    print("En la posicion", ingreso, "se encuentra el elemento", lista[ingreso])

main()