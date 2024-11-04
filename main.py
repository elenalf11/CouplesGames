'''
Clase Main

Esta clase es la clase es la clase principal del juego. Aquí se inicializa todo el flujo del juego.

Importaciones:

- board: Un objeto de la clase Board, será el tablero del juego
- engine: Un objeto de la clase Engine, será el control del flujo del juego
'''
from board import Board
from engine import Engine

class Main:

    '''
    Constructora de la clase Main.
    '''
    def __init__(self):
        pass
    
    #Variable para acabar el bucle de creación de tableros
    correcto = False

    print("------ Bienvenido al Juego de las Parejas -------")
    while(correcto == False):

        #El usuario introduce cuántas filas y cuántas columnas quiere en su juego.
        filas = int(input("Dime cuantas filas quieres que tenga el tablero: "))
        columnas = int(input("Dime cuantas columnas quieres que tenga el tablero: "))

        #Se crea el objeto de la clase Board, se necesita las filas y columnas que acaba de introducir el usuario por consola 
        tablero = Board(filas, columnas)

        #Se comprueban los datos introducidos por el usuario
        if(tablero.checkTablero()):
            #Si los datos son correctos se finaliza el bucle de la creación del tablero
            correcto = True
        else:
             #Si los datos no son correctos se vuelven a pedir
             print("Datos incorrectos, vuelve a intentarlo")
             correcto = False
       
    #Creación del objeto de la clase Engine, se necesita el tablero creado anteriormente.
    play = Engine(tablero)

    #Comienza el juego
    play.start()