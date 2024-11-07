'''
Clase Player

En esta clase estarán todos los métodos y atributos relacionados sobre los jugadores.

Importaciones:
- random: será utilizado para la jugabilidad de la CPU
'''
import random

class Player:

    '''
    Construtura de la clase Player. 
    
    Parámetros: 
    - nombre: es el nombre que introduce el usuario.
    - isCPU: es una variable boolena para identificar si el jugador es una CPU o un jugador real

    Atributos:

    - nombre: es el nombre del jugador 
    - points: son los puntos que obtiene el jugador durante el juego, se inicia en 0 puntos
    - parejas: son las parejas que adivina el jugador durante el juego, se inicia en 0 parejas
    - isCPU: es una varible booleana para identificar si el jugador es una CPU o un jugador real
    '''
    def __init__(self, name, isCPU):
        self.nombre = name
        self.points = 0
        self.parejas = 0
        self.isCPU = isCPU

    '''
    Función sumaPuntos
    
    Suma 2 puntos al jugador, se activará este método cuando el jugador o CPU adivine una pareja en el juego
    '''
    def sumaPuntos(self):
        #Se suman dos puntos al jugador 
        self.points += 2
    
    '''
    Función getName

    Devuelve el nombre del jugador.

    Return: nombre del jugador
    '''
    def getName(self):
        #Devuelve el nombre del jugador
        return self.nombre
    
    '''
    Función getPoints

    Devuelve la puntuación del jugador.

    Return: puntuación del jugador
    '''
    def getPoints(self):
        #Devuelve los puntos del jugador
        return self.points
    
    '''
    Función sumaParejas

    Suma 1 a las parejas del jugador, se activará este método cuando el jugador o CPU adivine una pareja en el juego
    '''
    def sumaParejas(self):
        #Se suma 1 pareja al jugador
        self.parejas += 1
    
    '''
    Función getParejas

    Devuelve las parejas que ha adivinado el jugador durante la partida.

    Return: las parejas que ha adivinado el jugador durante la partida.
    '''
    def getParejas(self):
        #Devuelve las parejas obtenidas por el jugador
        return self.parejas
    
    '''
    Función playCPU

    Genera las dos coordenas de la CPU. Esta función se activará en el modo de jugador vs CPU y en el modo de CPU vs CPU.
    Se genera mediante el método randint(x, y) de la biblioteca random

    Parámetros:
    - filas: son las filas del tablero
    - columnas: son las columnas del tablero

    Return: Devuelve una tupla con la coordenada de un icono
    '''
    def playCPU(self, filas, columnas):
        #Se genera la coordenada de las filas (posicion1, x)
        posicion1 = random.randint(0, (filas - 1))
        #Se genera la coordenada de las columnas (x, posicion2)
        posicion2 = random.randint(0, (columnas - 1))

        #Devuelve la coordenada completa
        return (posicion1, posicion2)
    
    def esCPU(self):
        return self.isCPU