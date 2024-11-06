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
                    player1 = Player(n1)

                    #Cración de player2
                    n2 = input("Hola jugador 2, ¿cuál es tu nombre?: ")
                    player2 = Player(n2)

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

                    #Se comienza a jugar con el jugador y la cpu (player y cpu)
                    self.play_2(player, cpu)

                    #Se finaliza el bucle del "menú"
                    check = True

                #Opción 3: Modo CPU vs CPU
                case 3 :
                    print("Has elegido el modo CPU vs CPU")
                    print("Lo siento, este modo todavía está en desarrollo")

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
                except:
                    #Si los datos introducidos anteriormente en el bloque try lanzan una excepción, esta la captura e imprime este mensaje por consola
                    print("Los datos no son correctos")
                
            #Se comprueba que las anteriores 4 posiciones conforman una pareja
            if(self.board.comprobarPareja(F1, C1, F2, C2) == True):
                #Consigue pareja el jugador 1
                if(cambioJugador == True):
                    print(f"¡Enhorabuena! {player1.getName()}, has conseguido una pareja. +2 puntos")
                    #Se le suman 2 puntos a su cuenta personal
                    player1.sumaPuntos()
                    #Se le suma 1 pareja a su cuenta personal
                    player1.sumaParejas()
                    #Este contador es para saber cuando ya se hayan acertado todas las parejas, por lo tanto al descubrir una pareja suma 1.
                    contador += 1
                    #"Limpia" la consola de código para que no se pueda hacer trampas
                    input()
                    self.clear()
                #Consigue pareja el jugador 2
                else:
                    print(f"¡Enhorabuena! {player2.getName()}, has conseguido una pareja. +2 puntos")
                    #Se le suman 2 puntos a su cuenta personal
                    player2.sumaPuntos()
                    #Se le suma 1 pareja a su cuenta personal
                    player2.sumaParejas()
                    #Este contador es para saber cuando ya se hayan acertado todas las parejas, por lo tanto al descubrir una pareja suma 1.
                    contador += 1
                    #"Limpia" la consola de código para que no se pueda hacer trampas
                    input()
                    self.clear()
            else:
                #El jugador 1 no consigue pareja
                if(cambioJugador == True):
                    print(f"Lo siento {player1.getName()}, no has conseguido la pareja. Pierdes tu turno")
                    #El turno pasa al jugador 2
                    cambioJugador = False
                    #"Limpia" la consola de código para que no se pueda hacer trampas
                    input()
                    self.clear()
                #El jugador 2 no consigue pareja
                else:
                    print(f"Lo siento {player2.getName()}, no has conseguido la pareja. Pierdes tu turno")
                    #El turno pasa al jugador 1
                    cambioJugador = True
                    #"Limpia" la consola de código para que no se pueda hacer trampas
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
    '''
    Función play_2

    Lleva a cabo todo el flujo del juego. Durante el modo jugador vs CPU

    Parámetros:
    - player: será el jugador real
    - cpu: será la máquina
    '''
    def play_2(self, player:Player, cpu:Player):
        #Este array se usará para próximas funcionalidades
        posiciones = []

        #Variable para acabar el juego
        acabar = False

        #Contador de parejas, para saber cuando acaba el juego
        contador = 0

        #Variable para ir cambiando de turno
        cambioJugador = True
        
        #Creación de tableros
        self.board.crearTableroX()
        self.board.crearTableroIconos()

        while(acabar == False):
            
            #Aquí se maneja el flujo del cambio de turnos
            if(cambioJugador == True):
                print(f"{player.getName()} es tu turno. Puntuación: {player.getPoints()} puntos. Parejas: {player.getParejas()} parejas")
            else:
                print(f"{cpu.getName()} es tu turno. Puntuación: {cpu.getPoints()} puntos. Parejas: {cpu.getParejas()} parejas")
            
            self.board.imprimirTableroX()
            ok1 = False
            #Este es el bucle para el primer icono. En este caso solo lo realiza el jugador real.
            while(ok1 == False):
                #Codigo para el jugador
                if(cambioJugador == True):
                    #Iniciamos un bloque try, por si ocurre un error poderlo manejar de una manera más sencilla
                    try:
                        #El -1 sirve para que el usuario pueda introducir los valores sin tener en cuenta el 0 del tablero, es decir, con números reales (1 -> longitud tablero)
                        F1 = int(input("Dime que fila quieres revelar: ")) -1
                        C1 = int(input("Dime que columna quieres revelar: ")) -1

                        #Comprobamos que los datos sean correctos, es decir que sea mayor que 0, que no supere la longitud del tablero y si existe un icono o no.
                        if((F1 < 0 or F1 > len(self.board.getTablero())) or (C1 < 0 or C1 > len(self.board.getTablero()[0])) or self.board.existeIcono(F1, C1)):
                            print("Datos incorrectos, vuelve a intentarlo")
                            ok1 = False
                            #El continue hace que el usuario vuelva a introducir los datos correctamente. Esto es muy útil ya que así te aseguras que todos los bucles funcionen correctamente
                            continue
                        else:
                            #Se muestra el icono que conforma las posiciones dadas por el usuario.
                            self.board.muestraIconos(F1, C1)
                            #Se imprime el tablero X, con el icono
                            self.board.imprimirTableroX()
                            ok1 = True
                    except:
                        #Si los datos introducidos anteriormente en el bloque try lanzan una excepción, esta la captura e imprime este mensaje por consola
                        print("¡Ups! Ha ocurrido un error")
                else:
                    #Este bloque se pone porque la CPU solo va a intervenir en un solo bucle, ya que dará coordenadas completas
                    ok1 = True
            
            ok2 = False
            #Este es el bucle para el segundo icono del jugador. Y también es el bucle en el que la cpu introduce sus valores
            while(ok2 == False):
                #Codigo para el jugador
                if(cambioJugador == True):
                    #Iniciamos un bloque try, por si ocurre un error poderlo manejar de una manera más sencilla
                    try:
                        #El -1 sirve para que el usuario pueda introducir los valores sin tener en cuenta el 0 del tablero, es decir, con números reales (1 -> longitud tablero)
                        F2 = int(input("Dime que fila quieres revelar: ")) -1
                        C2 = int(input("Dime que columnas quieres revelar: ")) -1

                        #Comprobamos que los datos sean correctos, es decir que sea mayor que 0, que no supere la longitud del tablero y si existe un icono o no.
                        if((F2 < 0 or F2 > len(self.board.getTablero())) or (C2 < 0 or C2 > len(self.board.getTablero()[0])) or self.board.existeIcono(F2, C2)):
                            print("Datos incorrectos, vuelve a intentarlo")
                            ok2 = False
                            #El continue hace que el usuario vuelva a introducir los datos correctamente. Esto es muy útil ya que así te aseguras que todos los bucles funcionen correctamente
                            continue
                        else:
                            #Se muestra el icono que conforma las posiciones dadas por el usuario.
                            self.board.muestraIconos(F2, C2)
                            #Se imprime el tablero X, con el icono
                            self.board.imprimirTableroX()
                            ok2 = True
                    except:
                        #Si los datos introducidos anteriormente en el bloque try lanzan una excepción, esta la captura e imprime este mensaje por consola
                        print("¡Ups! Ha ocurrido un error")
                   
                    
                #Codigo para la cpu
                else:
                    #La cpu genera una coordenada completa, esta es la coordenada del primer icono
                    cpuPos1 = cpu.playCPU(len(self.board.getTablero()), len(self.board.getTablero()[0]))
                    #Esta es la corrdenada del segundo icono
                    cpuPos2 = cpu.playCPU(len(self.board.getTablero()), len(self.board.getTablero()[0]))
                    
                    #Se comprueba que las coordenadas introducidas no contengan iconos ni que sean las dos coordenadas iguales
                    if((self.board.existeIcono(cpuPos1[0], cpuPos1[1]) == True) or (self.board.existeIcono(cpuPos2[0], cpuPos2[1]) == True) or cpuPos1 == cpuPos2):
                        ok2 = False
                        #El continue hace que la cpu genere nuevas coordenadas ya que las anteriores eran incorrectas
                        continue
                    else:
                        #Se muestra un mensaje para poder ver cuáles son las coordenadas de la cpu
                        print(f"La posicion 1 de {cpu.getName()} es ({cpuPos1[0] + 1}, {cpuPos1[1] + 1})")
                        print(f"La posición 2 de {cpu.getName()} es ({cpuPos2[0] + 1}, {cpuPos2[1] + 1})")

                        #Se muestra el primer icono
                        self.board.muestraIconos(cpuPos1[0], cpuPos1[1])
                        #Se muestra el segundo icono
                        self.board.muestraIconos(cpuPos2[0], cpuPos2[1])
                        #Se imprime el tablero X, con los iconos
                        self.board.imprimirTableroX()
                        ok2 = True

            #Codigo para el jugador
            if(cambioJugador == True):

                #Comprueba que las posiciones que ha introducido el jugador conformen una pareja
                if(self.board.comprobarPareja(F1, C1, F2, C2) == True):

                    print(f"¡Enhorabuena {player.getName()}, has conseguido una pareja! +2 puntos")

                    #Se suman 2 puntos a su cuenta personal
                    player.sumaPuntos()
                    #Se le suma 1 pareja a su cuenta personal
                    player.sumaParejas()
                    #Este contador es para saber cuando ya se hayan acertado todas las parejas, por lo tanto al descubrir una pareja suma 1.
                    contador += 1

                    #"Limpia" la consola de código para que no se pueda hacer trampas
                    input()
                    self.clear()
                #El jugador no consigue pareja
                else:

                    print(f"Lo siento {player.getName()}, no has conseguido pareja. Pierdes el turno")

                    #Cambia de turno a la cpu
                    cambioJugador = False

                    #"Limpia" la consola de código para que no se pueda hacer trampas
                    input()
                    self.clear()
            #Código para la cpu
            else:

                #Comprueba que las posiciones que ha generado la cpu conformen una pareja
                if(self.board.comprobarPareja(cpuPos1[0], cpuPos1[1], cpuPos2[0], cpuPos2[1]) == True):

                    print(f"¡Enhorabuena {cpu.getName()}, has conseguido una pareja! +2 puntos")

                    #Se suman 2 puntos a su cuenta personal
                    cpu.sumaPuntos()
                    #Se le suma 1 pareja a su cuenta personal
                    cpu.sumaParejas()
                    #Este contador es para saber cuando ya se hayan acertado todas las parejas, por lo tanto al descubrir una pareja suma 1.
                    contador += 1

                    #"Limpia" la consola de código para que no se pueda hacer trampas
                    input()
                    self.clear()
                #La cpu no consigue pareja
                else:
                    print(f"Lo siento {cpu.getName()}, no has conseguido pareja. Pierdes el turno")

                    #Cambia de turno al jugador
                    cambioJugador = True

                    #"Limpia" la consola de código para que no se pueda hacer trampas
                    input()
                    self.clear()
            
            #Comprueba que se hayan descubierto todas las parejas del tablero
            if(contador == self.board.getParejas()):

                #El jugador real consigue más puntos que la cpu. Gana el jugador real
                if(player.getPoints() > cpu.getPoints()):
                    print(f"¡Enhorabuena {player.getName()}! Has ganado la partida. Has conseguido un total de {player.getPoints()} puntos (El equivalente a {player.getParejas()} parejas). En cambio, {cpu.getName()} ha conseguido solo {cpu.getPoints()} puntos (El equivalente a {cpu.getParejas()} parejas)")
                    #Se acaba el juego
                    acabar = True
                
                #La cpu consigue más puntos que el jugador real. Gana la cpu
                elif(cpu.getPoints() > player.getPoints()):
                    print(f"¡Enhorabuena {cpu.getName()}! Has ganado la partida. Has conseguido un total de {cpu.getPoints()} puntos (El equivalente a {cpu.getParejas()} parejas). En cambio, {player.getName()} ha conseguido solo {player.getPoints()} puntos (El equivalente a {player.getParejas()} parejas)")
                    #Se acaba el juego
                    acabar = True
                
                #La cpu y el jugador real consiguen los mismos puntos. Empatan la cpu y el juador real
                else:
                    print(f"Eso si que no me lo esperaba! {player.getName()} y {cpu.getName()} habéis empatado con {player.getPoints()} puntos (El equivalente a {player.getParejas()} parejas) y {cpu.getPoints()} puntos (El equivalente a {cpu.getParejas()} parejas)")
                    #Se acaba el juego
                    acabar = True