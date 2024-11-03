'''
Clase Board

En esta clase estarán todos los métodos y atributos relacionados con los tableros de juego
'''
import random
class Board:

    '''
    Constructora de la clase Board. Parámetros: número de filas y columnas que inserta el usuario.

    Atributos:

    - Lista de iconos: es la lista que incluye todos los iconos que se van a emplear para buscar las parejas.
    - Lista de tablero jugable: es la lista en la que se encuentran todas las parejas de los iconos de manera descolocada.
    - Lista de tablero: es la lista en la que se encuentra "las cartas del revés" están representadas con una "X".
    - Parejas: es el número real de parejas que hay en la partida
    '''
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.iconos = ["🥥", "💷", "💧", "🎭", "🎅", "🏀", "🍏", "🐨", "🍀", "🌺", "🐸", "🦁", "👁️", "🧠", "🦴"]
        self.tablero_jugable = []
        self.tablero = []
        self.parejas = (filas * columnas)//2

    '''
    Función checkTablero

    Comprueba que el número de filas y columnas como mínimo sea 2. También comprueba si el tablero
    que el usuario quiere crear sea número par, para poder crear las parejas correctamente.

    Es una función booleana. Devuelve True si se cumple lo anteriormente dicho, sino, devuelve False.
    '''
    def checkTablero(self):
        multiplicacion = self.filas * self.columnas
        if((self.filas >= 2 and self.columnas >= 2) and (multiplicacion % 2 == 0) and (multiplicacion < 36)):
            return True
        else:
            return False
    
    '''
    Función crearTableroX

    Crea el tablero de las "cartas del revés". Es decir, rellena todas las posiciones con una "X".
    '''
    def crearTableroX(self):
        if(self.checkTablero()):
            self.tablero = [["X" for _ in range(self.columnas)] for _ in range(self.filas)]
            return self.tablero
    
    '''
    Función imprimirTableroX

    Imprime por consola el tablero de las "cartas del revés", el cual tiene en todas sus posiciones una "X".
    '''
    def imprimirTableroX(self):
       for fila in self.tablero:
           print(" ".join(fila))

    '''
    Función crearTableroIconos

    Crea el tablero que contiene todas las parejas descolocadas. 
    Para "descolocar" las parejas he empleado el método sample(x, len(y)) de la biblioteca random, el cual crea una nueva
    lista desordenada a partir de la original sin modificarla.
    '''
    def crearTableroIconos(self):
       if(self.checkTablero()):
            tablero = []
            for i in range(0, self.parejas):
                tablero.extend([self.iconos[i], self.iconos[i]])
                tablero_mezclado = random.sample(tablero, len(tablero))

                self.tablero_jugable = [tablero_mezclado[i:i + self.columnas] for i in range(0, len(tablero_mezclado), self.columnas)]
            return self.tablero_jugable


    '''
    Función imprimirTableroIconos

    Imprime por consola el tablero que contiene todas las parejas.
    '''
    def imprimirTableroIconos(self):
        for fila in self.tablero_jugable:
            print(" ".join(fila))
    
    '''
    Función maxParejas

    Define cuál es el número de parejas que ha de conseguir un jugador para ganar la partida.

    Return: el número de parejas que ha de conseguir un jugador para ganar la partida.
    '''
    def maxParejas(self):
        return self.parejas//2 + 1
    
    '''
    Función muestraParejas

    Muestra las parejas del tablero, con las posiciones que diga el usuario.

    Parámetros:
    - posicion: Es la tupla de la posición elegida por el usuario, (fila, columna)
    '''
    def muestraParejas(self, posicion):
        self.tablero[posicion[0]][posicion[1]] = self.tablero_jugable[posicion[0]][posicion[1]]

    '''
    Función getTablero

    Devuelve el tablero con las parejas.

    Return: el tablero que contiene las parejas
    '''   
    def getTablero(self):
        return self.tablero_jugable
    
    def existePareja(self, posicion):
        if(self.tablero[posicion[0]][posicion[1]] != "X"):
            return True
        else:
            return False
        
    def comprobarPareja(self, posicion1, posicion2):
        if(posicion1 != posicion2):
            if(self.tablero[posicion1[0]][posicion1[1]] == self.tablero[posicion2[0]][posicion2[1]]):
                return True
            else:
                self.quitarPareja(posicion1, posicion2)
                return False
        return False
       
    
    def quitarPareja(self, posicion1, posicion2):
        self.tablero[posicion1[0]][posicion1[1]] = "X"
        self.tablero[posicion2[0]][posicion2[1]] = "X"