'''
Clase Board

En esta clase estarán todos los métodos y atributos relacionados con los tableros de juego

Importaciones:

- random: será utilizado para descolocar las parejas por el tablero
'''
import random
class Board:

    '''
    Constructora de la clase Board. 
    
    Parámetros: 
    
    - filas: número de filas que inserta el usuario 
    - columnas: número de columnas que inserta el usuario.

    Atributos:

    - iconos: es la lista que incluye todos los iconos que se van a emplear para buscar las parejas.
    - tablero_jugable: es la lista en la que se encuentran todas las parejas de los iconos de manera descolocada.
    - tablero: es la lista en la que se encuentra "las cartas del revés" están representadas con una "X".
    - parejas: es el número real de parejas que hay en la partida
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

    Return: Devuelve True si se cumple lo anteriormente dicho, sino, devuelve False.
    '''
    def checkTablero(self):
        #Se hace la multiplicación de las filas y columnas para ver cuántas celdas habrá en el tablero
        multiplicacion = self.filas * self.columnas

        #Instrucción que se debe cumplir: Tablero mínimo (2x2) Tablero máximo(5x6 / 6x5)
        if((self.filas >= 2 and self.columnas >= 2) and (multiplicacion % 2 == 0) and (multiplicacion < 36)):
            #Si lo cumple devuelve True
            return True
        else:
            #Si no lo cumple devuelve False
            return False
    
    '''
    Función crearTableroX

    Crea el tablero de las "cartas del revés". Es decir, rellena todas las posiciones con una "X".

    Return: Devuelve el tablero de las "cartas del revés" o tablero X
    '''
    def crearTableroX(self):
        #Se rellena el tablero X con "X" con un doble bucle for que rellena columnas y filas
        self.tablero = [["X" for _ in range(self.columnas)] for _ in range(self.filas)]
        #Devuelve el tablero que se acaba de crear
        return self.tablero
    
    '''
    Función imprimirTableroX

    Imprime por consola el tablero de las "cartas del revés", el cual tiene en todas sus posiciones una "X".
    '''
    def imprimirTableroX(self):
       #Se imprime el tablero X, a través de un bucle for que imprime fila a fila.
       for fila in self.tablero:
           print("   ".join(fila))

    '''
    Función crearTableroIconos

    Crea el tablero que contiene todas las parejas descolocadas. 
    Para "descolocar" las parejas he empleado el método sample(x, len(y)) de la biblioteca random, el cual crea una nueva
    lista desordenada a partir de la original sin modificarla.

    Return: Devuelve el tablero_jugable, que es el tablero de los iconos
    '''
    def crearTableroIconos(self):
        #Se inicializa el array del tablero
        tablero = []

        #Se crea un bucle for que va de 0 hasta el número de parejas que se van a crear en el programa
        for i in range(0, self.parejas):
            #Se añaden las parejas por duplicado, es decir, un mismo icono se añade dos veces, para poder crear las parejas
            tablero.extend([self.iconos[i], self.iconos[i]])

            #Se crea un nuevo tablero en el cual se van a descolocar todas las parejas mediante random.sample(x, len(x))
            tablero_mezclado = random.sample(tablero, len(tablero))

            #Con el tablero original se rellena con la variable anterior, mediante sublistas que van desde 0 hasta el número de columnas que hay en el tablero.
            self.tablero_jugable = [tablero_mezclado[i:i + self.columnas] for i in range(0, len(tablero_mezclado), self.columnas)]
        
        #Devuelve el tablero tablero_jugable, que es el tablero de los iconos.
        return self.tablero_jugable


    '''
    Función imprimirTableroIconos

    Imprime por consola el tablero que contiene todas las parejas.
    '''
    def imprimirTableroIconos(self):
        #Se imprime el tablero de los iconos, a través de un bucle for que imprime fila a fila
        for fila in self.tablero_jugable:
            print(" ".join(fila))
    
    '''
    Función getParejas

    Define cuáles son el número de parejas del tablero, para saber cuando acabar la partida

    Return: el número de parejas del tablero 
    '''
    def getParejas(self):
        #Devuelve el número de parejas que hay en el tablero
        return self.parejas
    
    '''
    Función muestraIconos

    Muestra los iconos del tablero, con las posiciones que diga el usuario.

    Parámetros:

    - posicion1: Es la fila que introduce el usuario por consola
    - posicion2: Es la columna que introduce el usuario por consola
    '''
    def muestraIconos(self, posicion1, posicion2):
        #El tablero X sustituye una posición por una celda del tablero de los iconos
        self.tablero[posicion1][posicion2] = self.tablero_jugable[posicion1][posicion2]

    '''
    Función getTablero

    Devuelve el tablero con las parejas.

    Return: el tablero que contiene las parejas
    '''   
    def getTablero(self):
        #Devuelve el tablero de los iconos
        return self.tablero_jugable
    
    '''
    Función existeIcono

    Comprueba que la celda seleccionada sea un icono o una X.

    Parámetros:
    - posicion1: Es la fila que introduce el usuario por consola
    - posicion2: Es la columna que introduce el usuario por consola

    Return: si en esa celda hay un icono se retorna True, de lo contrario, devuelve False
    '''
    def existeIcono(self, posicion1, posicion2):
        #Comprueba que en la celda que el usuario ha indicado haya un icono
        if(self.tablero[posicion1][posicion2] != "X"):
            #Devuelve True si lo cumple
            return True
        else:
            #Devuelve False si no lo cumple
            return False
    
    '''
    Función comprobarPareja

    Comprueba que dos celdas contengan el mismo icono

    Parámetros:
    - posicion1: Es la fila 1 que introduce el usuario por consola
    - posicion2: Es la columna 1 que introduce el usuario por consola
    - posicion3: Es la fila 2 que introduce el usuario por consola
    - posicion4: Es la columna 2 que introuduce el usuario por consola

    Return: si las dos celdas coinciden se retorna True, de lo contrario, devuelve False y se cubre la pareja incorrecta
    '''
    def comprobarPareja(self, posicion1, posicion2, posicion3, posicion4):
        #Comprueba que la celda 1 y la celda 2 contengan el mismo icono
        if(self.tablero[posicion1][posicion2] == self.tablero[posicion3][posicion4]):
            #Si lo cumple devuelve True
            return True
        else:
            #Si no lo cumple cumbre los iconos en el tablero X
            self.quitarPareja(posicion1, posicion2, posicion3, posicion4)
            #Devuelve False
            return False
       
    '''
    Función quitarPareja

    Oculta las posiciones de los iconos, cuando la pareja no se ha acertado.

    Parámetros:
    - posicion1: Es la fila 1 que introduce el usuario por consola
    - posicion2: Es la columna 1 que introduce el usuario por consola
    - posicion3: Es la fila 2 que introduce el usuario por consola
    - posicion4: Es la columna 2 que introduce el usuario por consola
    '''
    def quitarPareja(self, posicion1, posicion2, posicion3, posicion4):
        #En la celda 1 (posicion1 y posicion2) se sustituye por una "X"
        self.tablero[posicion1][posicion2] = "X"
        #En la celda 2 (posicion3 y posicion4) se sustituye por una "X"
        self.tablero[posicion3][posicion4] = "X"