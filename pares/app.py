# Alumno: Soto Véjar Raúl Sebastián

from flask import Flask, render_template
import cartas
import pares 

app = Flask(__name__)

victorias = {"JugadorA": 0, "JugadorB": 0}

@app.route("/")
def index(): #index o root o home page
    return render_template("index.html", carta="/static/images/back_blue.png")

@app.route("/game_on")
def game_on():
    #realizar el juego de baraja
    #llamar a una funcion que regrese: 
    #el diccionario de barajas del jugador A
    #el diccionario de barajas del jugador B
    # {1:"P_10.png",2:"C_3.png" ... 7:"T_9.png"}
    # el nombre del ganador
    # la mano del ganador
    # el puntaje del ganador
    cartasA, cartasB, jugadorA, jugadorB, txt_Ganador = pares.jugar_web()
    if jugadorA.ganador:
        victorias["JugadorA"] += 1
    elif jugadorB.ganador:
        victorias["JugadorB"] += 1
    return render_template("game_on.html", cartas_j1=cartasA, cartas_j2=cartasB, jugador1=jugadorA, jugador2=jugadorB, txtGanador=txt_Ganador, win_count=victorias)