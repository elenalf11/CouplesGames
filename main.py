'''
Clase Main

Esta clase es la clase es la clase principal del juego. Aquí se inicializa todo el flujo del juego
'''
from board import Board

class Main:

    '''
    Constructora de la clase Main.
    '''
    def __init__(self):
        pass

    name = input("¡Hola!, ¿cuál es tu nombre?: ")

    filas = int(input(f"{name}, dime cuántas filas quieres que haya en tu tablero: "))
    columnas = int(input(f"{name}, ahora cuántas columnas quieres que haya: "))
    tablero = Board(filas, columnas)

    if (tablero.checkTablero() == True):

        tablero.crearTableroX()
        tablero.crearTableroIconos()

        print("El tablero con las cartas al revés es: ")
        tablero.imprimirTableroX()

        print("El tablero con las parejas implementadas y descolocadas es: ")
        tablero.imprimirTableroIconos()
    else:
        

        while(tablero.checkTablero() == False ):
            print("Los datos introducidos son incorrectos, por favor vuelva a intentarlo con otros datos.")
            filas = int(input(f"{name}, dime cuántas filas quieres que haya en tu tablero: "))
            columnas = int(input(f"{name}, ahora cuántas columnas quieres que haya: "))
            tablero = Board(filas, columnas)

            tablero.checkTablero()

        tablero.crearTableroX()
        tablero.crearTableroIconos()

        print("El tablero con las cartas al revés es: ")
        tablero.imprimirTableroX()

        print("El tablero con las parejas implementas y descolocadas es: ")
        tablero.imprimirTableroIconos()