'''
Clase Engine

En esta clase estarán todos los métodos y atributos relacionados con el flujo del juego.
'''
from player import Player
from board import Board
class Engine:

    '''
    Constructora de la clase Engine
    '''
    def __init__(self, board:Board):
        self.board = board

    def start (self):
        check = False
        while(check == False):
            print(" 1 -- Modo Persona vs Persona \n 2 -- Modo Persona vs CPU \n 3 -- Modo CPU vs CPU \n 0 -- Salir del programa" )
            option = int(input("Dime tu opción: "))
           
            match(option):
                case 1:
                    print("Has elegido el modo Persona vs Persona.")
                    n1 = input("Hola jugador 1, ¿cuál es tu nombre?: ")
                    player1 = Player(n1)
                    n2 = input("Hola jugador 2, ¿cuál es tu nombre?: ")
                    player2 = Player(n2)
                    print(f"Comenzamos la partida entre {player1.getName()} vs {player2.getName()}")
                    self.play(player1, player2)
                    check = True
                case 2:
                    print("Has elegido el modo Persona vs CPU")
                    print("Lo siento, este modo todavía está en desarrollo")
                    check = True
                case 3 :
                    print("Has elegido el modo CPU vs CPU")
                    print("Lo siento, este modo todavía está en desarrollo")
                    check = True
                case 0:
                    print("Saliendo del programa ...")
                    check = True
                case _:
                    print("Opción válida, vuelve a intentarlo")

    '''
    Función clear

    Simula que limpia la terminal, para que se pueda jugar de una manera más sencilla y sin distracciones.
    '''        
    def clear(self):
        for i in range (50):
            print()

    '''
    Función play

    Lleva a cabo todo el flujo del juego.
    '''
    def play(self, player1:Player, player2:Player):
        posiciones = []
        perdido = False
        cambioJugador = True
        self.board.crearTableroX()
        self.board.crearTableroIconos()

        while(perdido == False):

            if(cambioJugador == True):
                print(f"{player1.getName()} es tu turno")
            else:
                print(f"{player2.getName()} es tu turno")

            for i in range(2):
                self.board.imprimirTableroX()

                revelaFila = int(input("Dime que fila quieres revelar: ")) -1
                revelaColumna = int(input("Dime que columna quieres revelar: ")) -1
                if((revelaFila >= 0 and revelaFila <= len(self.board.getTablero())) and (revelaColumna >= 0 and revelaColumna <= len(self.board.getTablero()[0])) and self.board.existePareja((revelaFila, revelaColumna)) == False):
                    posiciones.append((revelaFila, revelaColumna))
                    self.board.muestraParejas((revelaFila, revelaColumna))
                
            if(self.board.comprobarPareja(posiciones[0], posiciones[1])):
                if (cambioJugador == True):
                    print(f"¡Enhorabuena! {player1.getName()} has encontrado una pareja, +2 puntos. Puntuación actual: {player1.getPoints()}")
                    player1.sumaPuntos()
                else:
                    print(f"¡Enhorabuena! {player2.getName()} has encontrado una pareja, +2 puntos. Puntuación actual: {player2.getPoints()}")
                    player2.sumaPuntos()
            else:
                    
                if(cambioJugador == True):
                    print(f"¡Oh no! {player1.getName()} has fallado la pareja, has perdido el turno.")
                    cambioJugador = False
                else:
                    print(f"¡Oh no! {player2.getName()} has fallado la pareja, has perdido el turno.")
                    cambioJugador = True
                    

            
            
            
        


        

    
