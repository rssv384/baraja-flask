#!/usr/bin/env python
import random

class Jugador:
    mano = None
    pares = None
    tercias = None
    nombre = None
    victorias = None

    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.mano = list()
        self.pares = dict()
        self.tercias = dict()
        self.poker = dict()
        self.ganador = False
    
class Carta:
    palo = None
    simbolo = None
    valor = None

    def __init__ (self, palo, simbolo) -> None:
        self.palo = palo
        self.simbolo = simbolo 
        diccionario = { "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
                        'J':11,"Q":12,"K":13,"A":20,"JK":1 }
        self.valor = diccionario[simbolo] 

    def __repr__ (self):
        cadena = f'{self.simbolo}{self.palo}'
        return (cadena)

class Baraja:
    cartas = list()
    dicc_cartas= dict()

    def __init__(self) -> None:
        palos = ["T","P","D","C"]
        simbolos = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        #llenamos lista de cartas
        jk1 = Carta(None,"JK")
        jk2 = Carta(None,"JK")
        self.cartas.append(jk1)
        self.cartas.append(jk2)
        for p in palos:
            lista = []
            for s in simbolos:
                c = Carta(p,s)
                self.cartas.append(c)
                lista.append(c)
            self.dicc_cartas[p] = lista
        self.revolver_cartas()
        
    def revolver_cartas(self) -> None:
        random.shuffle(self.cartas)
        '''
        for i in range( len(self.cartas) ):
            j = random.randrange(54)
            temp = self.cartas[i]
            self.cartas[i] = self.cartas[j]
            self.cartas[j] = temp
        '''

    def __repr__(self):
        print(self.cartas)

