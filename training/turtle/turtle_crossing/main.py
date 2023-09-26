import time  # We use this to slow down our game loop
from turtle import Screen  # A turtle Screen object to set up our game window
from player import (
    Player,
)  # Our player class that represents the turtle crossing the road
from car_manager import CarManager  # Our car manager that handles all car-related logic
from scoreboard import Scoreboard  # The scoreboard to keep track of the player's level

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(
    0
)  # Stops automatic screen updates, we'll do it manually for more control

# Initialize our player, car manager and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for keypress events
screen.listen()
screen.onkey(player.go_up, "Up")  # When "Up" key is pressed, turtle moves up

# The main game loop
game_is_on = True
while game_is_on:  # This loop will continue to run as long as game_is_on is True
    time.sleep(0.1)  # Pause for 0.1 seconds; gives us a chance to see what's happening
    screen.update()  # Manually update the screen

    car_manager.create_car()  # Try to create a car (it has a 1/6 chance each loop iteration)
    car_manager.move_cars()  # Move all existing cars

    # Collision detection with car
    for car in car_manager.all_cars:  # Iterate over all existing cars
        if (
            car.distance(player) < 20
        ):  # Turtle's collision detection method, if < 20 it's a collision
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display "Game Over"

    # Check for successful crossing
    if player.is_at_finish_line():  # If player's y-coordinate is past a certain point
        player.go_to_start()  # Send the player back to the start
        car_manager.level_up()  # Increase the car speed
        scoreboard.increase_level()  # Increase the level on the scoreboard

    # Alternative Methods:
    # 1) We could have implemented a pause and resume feature using a different game state variable.
    # 2) Collision could have been pixel-perfect for more realism but may be computationally intensive.
    # 3) A state machine could be implemented for various game states like 'playing', 'paused', 'game_over'.
    # 4) Sounds or music could be added for more interaction.
    # 5) The level-up mechanics could be more complex, like adding more cars or introducing obstacles.

screen.exitonclick()  # Exits the game when the screen is clicked

#----------------------------------------------------------------------------------------------------------------------------

#PARTE DE PREGUNTAS DE LA TAREA:

#ANALISIS DEL CÓDIGO:
#¿Qué hacen time, turtle, Player, CarManager y Scoreboard? Investiga y comprende cada uno.
#       TIME: Es el que determina todas las variables o funciones relacionadas con el tiempo y con su mención. 
#       TURTLE: Es la biblioteca grafica de python que permite que se generen los graficos en nuestro juego.
#       PLAYER: Es la estructura que controla y gestiona nuestro avatar como tal, que es la tortuga, es nuestro personaje del juego con la libreria de turtle que cargamos al inicio, es lo que determina como se mueve el jugador y el que trae la posición incial del jugador y tambien cuando se cruza la linea de llegada como nivel completado
#       CARMANAGER: Es la estructura para los movimientos, aumentos de velocidad de los coches, la generación de los coches de derecha a izquierda así como de los niveles y sus dificultades en aumento, tambien la creación de los coches en movimiento y colores. Se encarga basicamente de todo lo relacionado al movimiento, generacion y dirección de los coches en el juego
#       SCOREBOARD: Es la estructura para la gestión de los niveles que se estan ejecutando, es como tal el que muestra el nivel del juego cada vez que avanza y también muestra cuando el juego se finalizó el famoso "game over"

#Examina cómo se configura la pantalla con el módulo turtle. ¿Por qué es importante desactivar las actualizaciones automáticas?
#       En Turtle, la pantalla se configura con turtle.Screen(). 
#       Si no se desactivan las actualizaciones automáticas se vuelve muy lento ya que se estaría actualizando constantemente.

#Observa cómo se inicializan los objetos  player, car_manager y scoreboard. ¿Para qué se utilizan?
#       PLAYER: Es como tal la tortuga que cruzará el camino hacia el extremo, tratando de evitar los autos, como tal puede considerarse este como el "avatar" del juego como el simbolo con el cual jugaremos en este 
#       CAR_MANAGER: Como tal, es el "adminsitrador" o código diseñado para controlar los autos que se presentan en cada nivel, es aquel que se encarga de gestionar la cantidad, la velocidad, el rumbo y los lapsos entre cada nivel que se presenta. Los genera, administra y los mueve con respecto a la velocidad asignada.
#       SCOREBOARD: Es aquel que se encarga de determinar los niveles, es decir lo de nivel1, nievel2, nivel3 . También es el encargado de determinar si la turtle pierde, sale la leyenda de game over y tambien es aquel que determina la posición del juego.

# screen.listen() y screen.onkey().
#       SCREEN.ONKEY: Recibe o escucha las entradas, es decir es la función que se ejecuta al momento en el cual nosotros damos click click en la flechita para avanzar. Es cuando una tecla en particular del teclado se presiona. 
#       SCREEN.LISTEN: Esta es una función que permite la escucha de eventos o presiones del teclado en la pantalla que se esta utilizando, osea la función de turtle cuando sale la pantalla blanca. 
#      Estas dos funciones son a la par, es decir el código necesita que primero se plantee el "screen listen" y despues el "screen. onkey" para que puedan realizar sus funciones a la par para poder tener el resultado del movimiento de la tortuga, en este caso hacia adelante.

#Del bucle principal del juego (while game_is_on:): ¿Qué hace cada línea de código? Desglosa su función.
#      1.  WHILE GAME IS ON: es el bucle principal del juego, para poder ejecutar los otros 3 codigos que forman parte del main que determinan el funcionamiento del juego
#      2.  TIME SLEEP: Esta linea se puede modificar, tiene .1 en el juego y lo que indica este número es la forma en la cual se pausa la tortuga, es decir si nosotros le damos click a la flecha hacia adelante, lo que hara despues de ese click y avance será una pequeña pausa para las interacciones con el bucle permitiendo así que las 3 partes que componen al codigo sucedan al mismo tiempo
#      3.  SCREEN UPDATE: Actualiza de una forma automatica la pantalla para que pueda tener un mejor control
#      4.  CAR MANAGER CREATE CAR: Este genera y administra la generación de los autos que estan saliendo de la parte derecha, es controlado por la lógica que determina por tiempo y por velocidad como aparecen los coches 
#      5.  CAR MANAGER MOVE CARS: Este comando como tal es el administrador de todos los coches en pantalla, que sigan el cursor programado y que sigan la misma relación del bucle que se determinó
#      6.  FOR CAR IN CAR MANAGER ALL CARS: Es el bucle de los autos que se estan moviendo
#      7.  IF CAR DISTANCE: Es la distancia entre la tortuga y el auto, si se encuentran a 20 unidades, el juego sigue adelante, sin embargo si es menor a 20 unidades se considera como juego fallido, la tortuga tuvo un accidente con el auto
#      8.  GAME IS ON: Es lo que detecta dicho choque entre auto+tortuga
#      9.  SCOREBOARD GAME OVER: Leyenda despues del choque sobre que el juego esta terminado
#      10. IF PLAYER IS AT FINISH LINE: Es la función que nos permite avanzar a los siguientes niveles, como tal es la meta donde se determina que la tortuga logró avanzar todo el camino evitando los choques con los autos y permitiendo avanzar al siguiente nivel
#      11. PLAYER GO TO START: Regresa a la tortuga al punto incial para poder avanzar con el siguiente nivel
#      12. CAR MANAGER LEVEL UP: Conforme vas avanzando de nivel la dificultad del juego incrementa y la dificultad del juego se determina con la velocidad de los automoviles y con la frecuencia con la cual estos aparecen en el camino, es para aumentar dificultad
#      13. SCOREBOARD INCREASE LEVEL: Incrementa el numero del nivel conforme se van logrando, como tal es el progreso del jugador dentro del juego

#MODIFICACIONES:
#Si aumentas el valor, ¿el juego se vuelve más rápido o más lento?
#       Se vuelve más lento, de hecho cruzando el nivel, es decir del nivel 1 al nivel dos no se nota la velocidad en aumento de los coches, así que al aumentar la cantidad en tiempo.sleep se alenta. Lo probe con .8 pero lo regrese a su cantidad original en .1

#¿Qué sucede si cambias la cantidad que se mueve hacia arriba?
#       Cambia la cantidad como de "saltos" Es decir al inicial estaba en 10 e iba pasito a pasito, pero si aumentas la distancia la tortuga da brincos en lugar de pasos. Hablando coloquialmente la distancia. Lo probe con 30 y avanzaba más lejos a pesar de solo ser un click 

#¿Puedes hacer que los autos aparezcan con menos frecuencia?
#       Se hace en "random_chance == 1" aquí se determina con la probabilidad que indiques, como tal aqui es donde se crea. La probabilidad de 1. Si queremos que esto cambie pudieramos ponerlo así:
#       random_chance = random.randint(1, 10)  # Roll the dice
#        if (random_chance == 1) Aquí ya es 1 sobre 10 en cuestión de probabilidad, ya disminuye de 6 elementos que tenia a q 10 elementos y si quisiera aumentar la velocidad sería menor a 6 tomando en cuenta el numero inicial del codigo.

#¿Puedes cambiar el lugar donde se muestra, su color o su tamaño?
#       Sería en la parte de self.write: ahi se puede cambiar el texto como tal, la leyenda que quieras que se muestre
#       En la parte de font, sería cambiar el tipo de tipografia de esta leyenda, comot al existen limitadas que acepte python, pero son las generales así como el tamaño de la fuente y si quieres que este en cursiva, negrita, inclinada, etc. Funciona un poco como un word.

#REFELXIÓN Y DISCUSIÓN:
# ¿Qué partes del código te resultaron más difíciles de entender? ¿Y cuáles más fáciles?
#       Considero que lo que me resultó más dificil de entender fue la velocidad de los autos, es decir conforme iba avanzando sober los niveles del juego, esta parte puede ser para mi la más complicada.

# Al modificar el juego, ¿qué cambios te parecieron que mejoraban el juego y cuáles no?
#       Consideraria que el cambio más significativo es la frecuencia en la cual aparecen los autos y la que considero que no mejoró tanto el juego fue sobre el color/tamaño de la tortuga, como tal no se me hace relevante para el juego.

# ¿Qué otros cambios te gustaría implementar si tuvieras más tiempo o conocimientos adicionales?
#       Podría ser muy increible poder determinar la orientación de la tortuga, es decir que no solo se pueda ir hacia adelante, si no que tambien pueda retroceder la tortuga o ir a la derecha o izquierda en lugar de un camino recto hacia la meta
#       También podría ser interesante que cada nivel se pudiera orientar en una dirección diferente, es decir que el nivel uno empezaran los autos de derecha a izquierda y que el nivel dos empezaran de izquierda a derecha o tal vez de una forma aleatoria para poder aumentar la dificultad


