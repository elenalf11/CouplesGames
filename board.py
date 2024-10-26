'''
Clase Board

En esta clase estarán todos los métodos y atributos relacionados con los tableros de juego
'''

class Board:

    '''
    Constructora de la clase Board. Parámetros: número de filas y columnas que inserta el usuario.

    Atributos:

    - Lista de iconos: es la lista que incluye todos los iconos que se van a emplear para buscar las parejas.
    - Lista de tablero jugable: es la lista en la que se encuentran todas las parejas de los iconos de manera descolocada.
    - Lista de tablero: es la lista en la que se encuentra "las cartas del revés" están representadas con una "X".
    '''
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.iconos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.tablero_jugable = []
        self.tablero = []

    '''
    Método checkTablero

    Este método comprueba que el número de filas y columnas como mínimo sea 2. También comprueba si el tablero
    que el usuario quiere crear sea número par, para poder crear las parejas correctamente.

    Es una función booleana. Devuelve True si se cumple lo anteriormente dicho, sino, devuelve False.
    '''
    def checkTablero(self):
        multiplicacion = self.filas * self.columnas
        if((self.filas >= 2 and self.columnas >= 2) and (multiplicacion % 2 == 0)):
            return True
        else:
            return False
    
    '''
    Metodo crearTableroX

    Este método crea el tablero de las "cartas del revés". Es decir, rellena todas las posiciones con una "X".
    '''
    def crearTableroX(self):
        if(self.checkTablero()):
            for i in range(0,self.filas):
                for j in range(0, self.columnas):
                    self.tablero.append("X")
        else:
            print("Datos inválidos")
    
    '''
    Metodo imprimirTableroX

    Este método imprime por consola el tablero de las "cartas del revés", el cual tiene en todas sus posiciones una "X".
    '''
    def imprimirTableroX(self):
        for i in range(0, self.filas):
            print(self.tablero[i*self.columnas:(i+1)*self.columnas])

    '''
    Metodo crearTableroIconos

    Este método crea el tablero que contiene todas las parejas descolocadas.
    '''
    def crearTableroIconos(self):
        print()
