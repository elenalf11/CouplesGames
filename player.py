'''
Clase Player

En esta clase estarán todos los métodos y atributos relacionados sobre los jugadores.
'''

class Player:

    '''
    Construtura de la clase Player. Parámetros: nombre del jugador que introduce el usuario.

    Atributos:
    - Nombre: es el nombre del jugador 
    - Points: son los puntos que obtiene el jugador durante el juego, se inicia en 0 puntos
    '''
    def __init__(self, name):
        self.nombre = name
        self.points = 0

    '''
    Función sumaPuntos
    
    Suma 2 puntos al jugador, se activará este método cuando el jugador o CPU adivine una pareja en el juego
    '''
    def sumaPuntos(self):
        self.points += 2
    
    '''
    Función getName

    Devuelve el nombre del jugador.

    Return: nombre del jugador
    '''
    def getName(self):
        return self.nombre
    
    '''
    Función getPoints

    Devuelve la puntuación del jugador.

    Return: puntuación del jugador
    '''
    def getPoints(self):
        return self.points

