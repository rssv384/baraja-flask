# baraja-flask
Juego de baraja francesa, donde el usuario jugará contra la computadora para ver quién logra la mejor mano.

Para jugar, es necesario activar el programa desde la consola
  - set FLASK_APP=app.py
  - flask run

para luego acceder al navegador en la dirección http://127.0.0.1:5000/ y jugar ahí.

Al iniciar, mostrará la parte de atrás de las cartas y un botón de iniciar. Al dar click en este, el programa repartirá al azar la mano del jugador y la de otro jugador (la computadora) mostrando las cartas que obtuvo cada quién (con su nombre en la parte superior de la "mano"), así como el puntaje de cada uno y deberá mostrar una leyenda con el nombre del jugador ganador y su puntuación.

La baraja francesa consta de 52 cartas distribuidas en 4 palos (corazones, diamantes, picas y tréboles), estos palos o conjuntos están conformados así: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack (paje), Queen (reina), King (rey) y Ace (as).  Para este ejercicio, Jack tendrá un valor de 11, Queen 12, King 13 y Ace 20.

Este programa fue desarrollado como parte de la clase de Desarrollo de Sistemas IV en la Universidad de Sonora.
