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
        acabar = False
        contador = 0
        cambioJugador = True
        self.board.crearTableroX()
        self.board.crearTableroIconos()

        while(acabar == False):

            if(cambioJugador == True):
                print(f"{player1.getName()} es tu turno. Puntuación: {player1.getPoints()} puntos")
            else:
                print(f"{player2.getName()} es tu turno. Puntuación: {player2.getPoints()} puntos")

            self.board.imprimirTableroX()
            ok1 = False
            while (ok1 == False):
                try:
                    p1F1 = int(input("Dime que fila quieres revelar: ")) -1
                    p1C1 = int(input("Dime que columna quieres revelar: ")) -1
                    if(((p1F1 < 0 or p1F1 > len(self.board.getTablero())) or (p1C1 < 0 or p1C1 > len(self.board.getTablero()[0]))) or self.board.existeIcono(p1F1, p1C1)):
                        print("Datos incorrectos, vuelve a introducirlos")
                        ok1 = False
                        continue
                        
                    else:
                        self.board.muestraParejas(p1F1, p1C1)
                        self.board.imprimirTableroX()
                        ok1 = True
                except:
                    print("Los datos no son correctos")
                
            
            ok2 = False
            while(ok2 == False):
                try:
                    p1F2 = int(input("Dime que fila quieres revelar: ")) -1
                    p1C2 = int(input("Dime que columna quieres revelar: ")) -1
                    if(((p1F2 < 0 or p1F2 > len(self.board.getTablero())) or (p1C2 < 0 or p1C2 > len(self.board.getTablero()[0]))) or self.board.existeIcono(p1F2, p1C2)):
                        print("Datos incorrectos, vuelve a introducirlos")
                        ok2 = False
                        continue
                        
                    else:
                        self.board.muestraParejas(p1F2, p1C2)
                        self.board.imprimirTableroX()
                        ok2 = True
                except:
                    print("Los datos no son correctos")
                

            if(self.board.comprobarPareja(p1F1, p1C1, p1F2, p1C2) == True):
                if(cambioJugador == True):
                    print(f"¡Enhorabuena! {player1.getName()}, has conseguido una pareja. +2 puntos")
                    player1.sumaPuntos()
                    contador += 1
                else:
                    print(f"¡Enhorabuena! {player2.getName()}, has conseguido una pareja. +2 puntos")
                    player2.sumaPuntos()
                    contador += 1
            else:
                if(cambioJugador == True):
                    print(f"Lo siento {player1.getName()}, no has conseguido la pareja. Pierdes tu turno")
                    cambioJugador = False
                else:
                    print(f"Lo siento {player2.getName()}, no has conseguido la pareja. Pierdes tu turno")
                    cambioJugador = True

            if(contador == self.board.getParejas()):
                if(player1.getPoints() > player2.getPoints()):
                    print(f"¡Enhorabuena {player1.getName()}! Has ganado la partida. Has conseguido un total de {player1.getPoints()} puntos")
                    acabar = True
                elif(player2.getPoints() > player1.getPoints()):
                    print(f"¡Enhorabuena {player2.getName()}! Has ganado la partida. Has conseguido un total de {player2.getPoints()} puntos")
                    acabar = True
                elif(player1.getPoints() == player2.getPoints()):
                    print(f"¡Eso si que no me lo esperaba! {player1.getName()} y {player2.getName()} habéis empatado con {player1.getPoints()} puntos y {player2.getPoints()} puntos")
                    acabar = True
            
            
            
