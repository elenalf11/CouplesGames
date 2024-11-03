'''
Clase Main

Esta clase es la clase es la clase principal del juego. Aquí se inicializa todo el flujo del juego
'''
from board import Board
from engine import Engine

class Main:

    '''
    Constructora de la clase Main.
    '''
    def __init__(self):
        pass
    
    correcto = False
    print("------ Bienvenido al Juego de las Parejas -------")
    while(correcto == False):
        filas = int(input("Dime cuantas filas quieres que tenga el tablero: "))
        columnas = int(input("Dime cuantas columnas quieres que tenga el tablero: "))
        
        if((filas >= 2 and columnas >= 2) and ((filas * columnas) % 2 == 0) and ((filas * columnas) < 36)):
            correcto = True
        else:
            print("Datos incorrectos, vuelve a intentarlo")
            correcto = False
    
    tablero = Board(filas, columnas)
    play = Engine(tablero)
    play.start()