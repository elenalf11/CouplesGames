'''
Clase Engine

En esta clase estarán todos los métodos y atributos relacionados con el flujo del juego.

Importaciones:

- player: Un objeto de la clase Player, serán los jugadores
- board: Un objeto de la clase Board, será el tablero del juego
'''
from player import Player
from board import Board

class Engine:

    '''
    Constructora de la clase Engine.

    Parámetros:
    - board: Un objeto de la clase Board, que se será el tablero del juego

    Atributos:
    - board: Un objeto de la clase Board, que será el tablero del juego
    '''
    def __init__(self, board:Board):
        self.board = board

    '''
    Función start

    Se muestran todas las opciones para jugar, el usuario debe seleccionar un modo de juego. Próximamente se implementará la dificultad
    '''
    def start (self):
        #Variable para finalizar el bucle del "menú"
        check = False
        while(check == False):
            #Se imprimen los modos de juego
            print(" 1 -- Modo Persona vs Persona \n 2 -- Modo Persona vs CPU \n 3 -- Modo CPU vs CPU \n 0 -- Salir del programa" )
            #El usuario selecciona el número del modo de juego que desea
            option = int(input("Dime tu opción: "))
           
           #Se crea un match para hacer más sencilla la selección de modos
            match(option):
                #Opción 1: Modo Persona vs Persona
                case 1:
                    print("Has elegido el modo Persona vs Persona.")

                    #Creación de player1
                    n1 = input("Hola jugador 1, ¿cuál es tu nombre?: ")
                    player1 = Player(n1, False)

                    #Cración de player2
                    n2 = input("Hola jugador 2, ¿cuál es tu nombre?: ")
                    player2 = Player(n2, False)

                    #Se comienza a jugar con los dos jugadores (player1 y player2)
                    self.play(player1, player2)

                    #Se finaliza el bucle del "menú"
                    check = True
                
                #Opción 2: Modo Persona vs CPU
                case 2:
                    print("Has elegido el modo Persona vs CPU")

                    #Creación de player
                    n = input("Hola jugador, ¿cuál es tu nombre?: ")
                    player = Player(n, False)

                    #Creación de cpu
                    cpu = Player("cpu", True)

                    #Aquí se preguntará la dificultad de la cpu

                    #Se comienza a jugar con el jugador y la cpu (player y cpu)
                    self.play(player, cpu)

                    #Se finaliza el bucle del "menú"
                    check = True

                #Opción 3: Modo CPU vs CPU
                case 3 :
                    print("Has elegido el modo CPU vs CPU")

                    cpu1 = Player("cpu1", True)
                    cpu2 = Player("cpu2", True)

                    #Aquí se preguntará la dificultad de la cpu

                    self.play(cpu1, cpu2)

                    #Se finaliza el bucle del "menú"
                    check = True

                #Opción 4: Salir
                case 0:
                    print("Saliendo del juego ...")

                    #Se finaliza el bucle del menú
                    check = True

                #Opción no válida, se vuelven a pedir los datos
                case _:
                    print("Opción incorrecta, vuelve a intentarlo")

    '''
    Función clear

    Simula que limpia la terminal, para que se pueda jugar de una manera más sencilla y sin distracciones.
    '''        
    def clear(self):
        #Se imprimen 50 líneas en blanco
        for i in range (50):
            print()

    '''
    Función play

    Lleva a cabo todo el flujo del juego. Durante el modo jugador vs jugador

    Parámetros: 
    - player1: jugador 1
    - player2: jugador 2
    '''
    def play(self, player1:Player, player2:Player):
        posiciones = []
        #Variable para acabar el juego
        acabar = False

        #Contador de parejas, para saber cuando se han adivinado todas
        contador = 0
        
        #Variable para cambiar de jugador
        cambioJugador = True

        #Creación de tableros
        self.board.crearTableroX()
        self.board.crearTableroIconos()

        while(acabar == False):
            #Aquí se maneja el flujo del cambio de jugador
            if(cambioJugador == True):
                print(f"{player1.getName()} es tu turno. Puntuación: {player1.getPoints()} puntos. Parejas: {player1.getParejas()} parejas")
            else:
                print(f"{player2.getName()} es tu turno. Puntuación: {player2.getPoints()} puntos. Parejas: {player2.getParejas()} parejas")

            self.board.imprimirTableroX()
            ok1 = False
            #Este es el bucle para el primer icono
            while (ok1 == False):
                if(cambioJugador == True):
                    if(player1.esCPU() == True):
                        ok1 = True
                    else:
                        #Con el try puedo manejar mejor el control de errores, ya que este bloque de código tendía a fallar.
                        try:
                            #El -1, sirve para que el usuario pueda introducir los valores sin tener en cuenta el 0 del tablero, es decir, con números reales (1 -> longitud tablero)
                            F1 = int(input("Dime que fila quieres revelar: ")) -1
                            C1 = int(input("Dime que columna quieres revelar: ")) -1
                            #Comprobamos que los datos sean correctos, es decir que sea mayor que 0, que no supere la longitud del tablero y si existe un icono o no.
                            if(((F1 < 0 or F1 > len(self.board.getTablero())) or (C1 < 0 or C1 > len(self.board.getTablero()[0]))) or self.board.existeIcono(F1, C1)):
                                print("Datos incorrectos, vuelve a introducirlos")
                                ok1 = False
                                #El continue hace que el usuario vuelva a introducir los datos correctamente. Esto es muy útil ya que así te aseguras que todos los bucles funcionen
                                continue
                        
                            else:
                                #Se muestra el icono que conforma las posiciones dadas por el usuario.
                                self.board.muestraIconos(F1, C1)
                                #Se imprime el tablero X, con el icono
                                self.board.imprimirTableroX()
                                ok1 = True
                        except:
                            #Si los datos introducidos anteriormente en el bloque try lanzan una excepción, esta la captura e imprime este mensaje por consola
                            print("Los datos no son correctos")
                else:
                    if(player2.esCPU() == True):
                        ok1 = True
                    else:
                        #Con el try puedo manejar mejor el control de errores, ya que este bloque de código tendía a fallar.
                        try:
                            #El -1, sirve para que el usuario pueda introducir los valores sin tener en cuenta el 0 del tablero, es decir, con números reales (1 -> longitud tablero)
                            F1 = int(input("Dime que fila quieres revelar: ")) -1
                            C1 = int(input("Dime que columna quieres revelar: ")) -1
                            #Comprobamos que los datos sean correctos, es decir que sea mayor que 0, que no supere la longitud del tablero y si existe un icono o no.
                            if(((F1 < 0 or F1 > len(self.board.getTablero())) or (C1 < 0 or C1 > len(self.board.getTablero()[0]))) or self.board.existeIcono(F1, C1)):
                                print("Datos incorrectos, vuelve a introducirlos")
                                ok1 = False
                                #El continue hace que el usuario vuelva a introducir los datos correctamente. Esto es muy útil ya que así te aseguras que todos los bucles funcionen
                                continue
                        
                            else:
                                #Se muestra el icono que conforma las posiciones dadas por el usuario.
                                self.board.muestraIconos(F1, C1)
                                #Se imprime el tablero X, con el icono
                                self.board.imprimirTableroX()
                                ok1 = True
                        except:
                            #Si los datos introducidos anteriormente en el bloque try lanzan una excepción, esta la captura e imprime este mensaje por consola
                            print("Los datos no son correctos")
    
            ok2 = False
            #Este es el bucle para el segundo icono
            while(ok2 == False):
                if(cambioJugador == True):
                    if(player1.esCPU() == True):
                        pos1cpu1 = player1.playCPU(len(self.board.getTablero()), len(self.board.getTablero()[0]))
                        pos2cpu1 = player1.playCPU(len(self.board.getTablero()), len(self.board.getTablero()[0]))

                        if((self.board.existeIcono(pos1cpu1[0], pos1cpu1[1])) == True or (self.board.existeIcono(pos2cpu1[0], pos2cpu1[1])) == True or pos1cpu1 == pos2cpu1):
                            ok2 = False
                            continue
                        else:
                            print(f"La posición 1 de {player1.getName()} es ({pos1cpu1[0] + 1}, {pos1cpu1[1] + 1})")
                            print(f"La posición 2 de {player1.getName()} es ({pos2cpu1[0] + 1}, {pos2cpu1[1] + 1})")
                    
                        self.board.muestraIconos(pos1cpu1[0], pos1cpu1[1])
                        self.board.muestraIconos(pos2cpu1[0], pos2cpu1[1])

                        self.board.imprimirTableroX()

                        ok2 = True
                    else:
                        #Con el try puedo manejar mejor el control de errores, ya que este bloque de código tendía a fallar.
                        try:
                            #El -1, sirve para que el usuario pueda introducir los valores sin tener en cuenta el 0 del tablero, es decir, con números reales (1 -> longitud tablero)
                            F2 = int(input("Dime que fila quieres revelar: ")) -1
                            C2 = int(input("Dime que columna quieres revelar: ")) -1

                            #Comprobamos que los datos sean correctos, es decir que sea mayor que 0, que no supere la longitud del tablero y si existe un icono o no.
                            if(((F2 < 0 or F2 > len(self.board.getTablero())) or (C2 < 0 or C2 > len(self.board.getTablero()[0]))) or self.board.existeIcono(F2, C2)):
                                print("Datos incorrectos, vuelve a introducirlos")
                                ok2 = False
                                #El continue hace que el usuario vuelva a introducir los datos correctamente. Esto es muy útil ya que así te aseguras que todos los bucles funcionen
                                continue
                        
                            else:
                                #Se muestra el icono que conforma las posiciones dadas por el usuario.
                                self.board.muestraIconos(F2, C2)
                                #Se imprime el tablero X, con el icono
                                self.board.imprimirTableroX()
                                ok2 = True
                                break
                        except:
                            #Si los datos introducidos anteriormente en el bloque try lanzan una excepción, esta la captura e imprime este mensaje por consola
                            print("Los datos no son correctos")
                else:
                    if(player2.esCPU() == True):
                        pos1cpu2 = player2.playCPU(len(self.board.getTablero()), len(self.board.getTablero()[0]))
                        pos2cpu2 = player2.playCPU(len(self.board.getTablero()), len(self.board.getTablero()[0]))

                        if((self.board.existeIcono(pos1cpu2[0], pos1cpu2[1])) == True or (self.board.existeIcono(pos2cpu2[0], pos2cpu2[1])) == True or pos1cpu2 == pos2cpu2):
                            ok2 = False
                            continue
                        else:
                            print(f"La posición 1 de {player2.getName()} es ({pos1cpu2[0] + 1}, {pos1cpu2[1] + 1})")
                            print(f"La posición 2 de {player2.getName()} es ({pos2cpu2[0] + 1}, {pos2cpu2[1] + 1})")

                            self.board.muestraIconos(pos1cpu2[0], pos1cpu2[1])
                            self.board.muestraIconos(pos2cpu2[0], pos2cpu2[1])

                            self.board.imprimirTableroX()

                            ok2 = True
                    else:
                        try:
                            #El -1, sirve para que el usuario pueda introducir los valores sin tener en cuenta el 0 del tablero, es decir, con números reales (1 -> longitud tablero)
                            F2 = int(input("Dime que fila quieres revelar: ")) -1
                            C2 = int(input("Dime que columna quieres revelar: ")) -1

                            #Comprobamos que los datos sean correctos, es decir que sea mayor que 0, que no supere la longitud del tablero y si existe un icono o no.
                            if(((F2 < 0 or F2 > len(self.board.getTablero())) or (C2 < 0 or C2 > len(self.board.getTablero()[0]))) or self.board.existeIcono(F2, C2)):
                                print("Datos incorrectos, vuelve a introducirlos")
                                ok2 = False
                                #El continue hace que el usuario vuelva a introducir los datos correctamente. Esto es muy útil ya que así te aseguras que todos los bucles funcionen
                                continue
                        
                            else:
                                #Se muestra el icono que conforma las posiciones dadas por el usuario.
                                self.board.muestraIconos(F2, C2)
                                #Se imprime el tablero X, con el icono
                                self.board.imprimirTableroX()
                                ok2 = True
                        except:
                            #Si los datos introducidos anteriormente en el bloque try lanzan una excepción, esta la captura e imprime este mensaje por consola
                            print("Los datos no son correctos")
            
            if(cambioJugador == True):
                if(player1.esCPU() == True):
                    if(self.board.comprobarPareja(pos1cpu1[0], pos1cpu1[1], pos2cpu1[0], pos2cpu1[1]) == True):
                        print(f"¡Enhorabuena {player1.getName()}!, has conseguido una pareja. +2 puntos")
                        player1.sumaPuntos()
                        player1.sumaParejas()
                        contador += 1
                        input()
                        self.clear()
                    else:
                        print(f"Lo siento {player1.getName()}, no has conseguido la pareja. Pierdes tu turno")
                        cambioJugador = False
                        input()
                        self.clear()
                else:
                    #Se comprueba que las anteriores 4 posiciones conforman una pareja
                    if(self.board.comprobarPareja(F1, C1, F2, C2) == True):
                        #Consigue pareja el jugador 1
                        print(f"¡Enhorabuena {player1.getName()}!, has conseguido una pareja. +2 puntos")
                        #Se le suman 2 puntos a su cuenta personal
                        player1.sumaPuntos()
                        #Se le suma 1 pareja a su cuenta personal
                        player1.sumaParejas()
                        #Este contador es para saber cuando ya se hayan acertado todas las parejas, por lo tanto al descubrir una pareja suma 1.
                        contador += 1
                        #"Limpia" la consola de código para que no se pueda hacer trampas
                        input()
                        self.clear()
                    else:
                        print(f"Lo siento {player1.getName()}, no has conseguido la pareja. Pierdes tu turno")
                        #El turno pasa al jugador 2
                        cambioJugador = False
                        #"Limpia" la consola de código para que no se pueda hacer trampas
                        input()
                        self.clear()
            else:
                if(player2.esCPU() == True):
                    if(self.board.comprobarPareja(pos1cpu2[0], pos1cpu2[1], pos2cpu2[0], pos2cpu2[1]) == True):
                        print(f"¡Enhorabuena {player2.getName()}!, has conseguido una pareja. +2 puntos")
                        player2.sumaPuntos()
                        player2.sumaParejas()
                        contador += 1
                        input()
                        self.clear()
                    else:
                        print(f"Lo siento {player2.getName()}, no has conseguido pareja. Pierdes tu turno")
                        cambioJugador = True
                        input()
                        self.clear()
                else:
                    #Se comprueban que las 4 anteriores posiciones conformen una pareja
                    if(self.board.comprobarPareja(F1, C1, F2, C2) == True):
                        print(f"¡Enhorabuena {player2.getName()}!, has conseguido una pareja. +2 puntos")
                        player2.sumaPuntos()
                        player2.sumaParejas()
                        contador += 1
                        input()
                        self.clear()
                    else:
                        print(f"Lo siento {player2.getName()}, no has conseguido pareja. Pierdes el turno")
                        cambioJugador = True
                        input()
                        self.clear()

            #Comprueba que se hayan descubierto todas las parejas del tablero
            if(contador == self.board.getParejas()):
                #El jugador 1 tiene más puntos que el jugador 2. Gana el jugador 1
                if(player1.getPoints() > player2.getPoints()):
                    print(f"¡Enhorabuena {player1.getName()}! Has ganado la partida. Has conseguido un total de {player1.getPoints()} puntos (El equivalente a {player1.getParejas()} parejas). En cambio {player2.getName()} ha conseguido solo {player2.getPoints()} puntos (El equivalente a {player2.getParejas()} parejas)")
                    #Se finaliza el juego
                    acabar = True

                #El jugador 2 tiene más puntos que el jugador 1. Gana el jugador 2
                elif(player2.getPoints() > player1.getPoints()):
                    print(f"¡Enhorabuena {player2.getName()}! Has ganado la partida. Has conseguido un total de {player2.getPoints()} puntos (El equivalente a {player2.getParejas()} parejas). En cambio {player1.getName()} ha conseguido solo {player1.getPoints()} puntos (El equivalente a {player1.getParejas()} parejas)")
                    #Se finaliza el juego
                    acabar = True

                #El jugador 1 y el jugador 2 han conseguido los mismos puntos. Hay un empate.
                else:
                    print(f"¡Eso si que no me lo esperaba! {player1.getName()} y {player2.getName()} habéis empatado con {player1.getPoints()} puntos (El equivalente a {player1.getParejas} parejas) y {player2.getPoints()} puntos (El equivalente a {player2.getParejas()} parejas)")
                    #Se finaliza el juego
                    acabar = True