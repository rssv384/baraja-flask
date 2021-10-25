import cartas 
import random 

def main(jugador_1, jugador_2):
    A,B = jugar()
    print(A.mano)
    print(B.mano)

def comprobar_manos(jugador) -> None:
    mano = jugador.mano
    diccionario = dict()
    for carta in mano:
        if carta.simbolo in diccionario:
            diccionario[carta.simbolo] += 1
        else:
            diccionario[carta.simbolo] = 1

    lista = []
    for key, value in diccionario.items():
        if value == 2 and key != "JK":
            lista = [c for c in jugador.mano if c.simbolo == key]
            jugador.pares[key] = lista
        elif value == 3 and key != "JK":
            lista = [c for c in jugador.mano if c.simbolo == key]
            jugador.tercias[key] = lista
        elif value == 4 and key != "JK":
            lista = [c for c in jugador.mano if c.simbolo == key]
            jugador.poker[key] = lista
    comprobar_joker(jugador)
    print(diccionario) 
    print("PARES -> ",jugador.pares)
    print("TERCIAS -> ",jugador.tercias)
    print("POKER -> ",jugador.poker)


def comprobar_joker(jugador):
    mano = [c.simbolo for c in jugador.mano]

    if "JK" in mano:
        num_jk = mano.count("JK")
        for i in range(num_jk):
            if len(jugador.tercias) > 0:
                tercias = [c for c in jugador.mano if c.simbolo in jugador.tercias]
                # Obtenemos la carta de mayor valor
                maxt = max(tercias, key=lambda c: c.valor)
                # Obtenmos el índice que ocupa el Joker en la mano y le asignamos el valor de la tercia mayor
                idx = mano.index("JK")
                jugador.mano[idx].valor = maxt.valor
                # Agregamos el Joker a la tercia de mayor valor para crear un poker (4 cartas del mismo simbolo)
                jugador.tercias[maxt.simbolo].append(jugador.mano[idx])
                # Extraemos el nuevo poker y la insertamos en el poker del jugador
                jugador.poker[maxt.simbolo] = jugador.tercias.pop(maxt.simbolo)

            elif len(jugador.pares) > 0:
                pares = [c for c in jugador.mano if c.simbolo in jugador.pares]
                # Obtenemos la carta de mayor valor
                maxp = max(pares, key=lambda c: c.valor)
                # Obtenmos el índice que ocupa el Joker en la mano y le asignamos el valor del par mayor
                idx = mano.index("JK")
                jugador.mano[idx].valor = maxp.valor
                # Agregamos el Joker al par de mayor valor para crear una tercia
                jugador.pares[maxp.simbolo].append(jugador.mano[idx])
                # Extraemos la nueva tercia y lo insertamos en las tercias del jugador
                jugador.tercias[maxp.simbolo] = jugador.pares.pop(maxp.simbolo)

            else:
                mano = [c for c in jugador.mano]
                # Obtenemos la carta de mayor valor
                maxm = max(mano, key=lambda c: c.valor)
                # Obtenmos el índice que ocupa el Joker en la mano y le asignamos el valor de la carta mayor
                idx  = mano.index("JK")
                jugador.mano[idx].valor = maxm.valor
                # Agregamos el par de la carta de mayor valor + joker a los pares del jugador
                jugador.pares[maxm.simbolo] = [maxm, jugador.mano[idx]]
            # Eliminar la primera ocurrencia de JK de la mano (no del atributo jugador.mano, sino de la lista creada al inicio de la función)
            # para que, en caso de contar con 2 JK, podamos trabajar con el segundo en la siguiente vuelta del ciclo for.
            # Nota: Esto es debido a que index() regresa la primera ocurrencia en la lista
            mano.remove("JK")


def definir_ganador(jugador_1, jugador_2):
    mano_j1, puntaje_j1, crit_desemp_j1 = obtener_mano(jugador_1)
    mano_j2, puntaje_j2, crit_desemp_j2 = obtener_mano(jugador_2)

    formato = "El ganador es el jugador {0} con la mano: {1}.\nTotal de puntos: {2}"

    if (puntaje_j1 > puntaje_j2):
        jugador_1.ganador = True
        print(formato.format(jugador_1.nombre,mano_j1,puntaje_j1))
        return formato.format(jugador_1.nombre,mano_j1,puntaje_j1)
    elif (puntaje_j2 > puntaje_j1):
        jugador_2.ganador = True
        print(formato.format(jugador_2.nombre,mano_j2,puntaje_j2))
        return formato.format(jugador_2.nombre,mano_j2,puntaje_j2)
    else:
        if (crit_desemp_j1 > crit_desemp_j2):
            jugador_2.ganador = True
            print(formato.format(jugador_1.nombre,mano_j1,puntaje_j1))
            return formato.format(jugador_1.nombre,mano_j1,puntaje_j1)
        elif (crit_desemp_j2 > crit_desemp_j1):
            jugador_2.ganador = True
            print(formato.format(jugador_2.nombre,mano_j2,puntaje_j2))
            return formato.format(jugador_2.nombre,mano_j2,puntaje_j2)

def obtener_mano(jugador):
    '''
                                             [Poker, Tercias, Pares]              Código                 Puntaje
    MANOS GANADORAS EN ORDEN DESCENDENTE:
        1 -> poker + 1 tercia ---------------------- [1,1,0] -------------------- "110" ---------------- 220
        2 -> poker + 1 par ------------------------- [1,0,1] -------------------- "101" ---------------- 210
        3 -> poker(cuatro del mismo simbolo) ------- [1,0,0] -------------------- "100" ---------------- 200
        4 -> full + 1 par -------------------------- [0,1,2] -------------------- "012" ---------------- 190
        5 -> full (tercia + 1 par) ----------------- [0,1,1] -------------------- "011" ---------------- 180
        6 -> color (todas cartas mismo palo)-------- [0,0,0] -------------------- "000" -> "CLR" ------- 170
        7 -> 2 tercias ----------------------------- [0,2,0] -------------------- "020" ---------------- 160
        8 -> 3 pares ------------------------------- [0,0,3] -------------------- "003" ---------------- 150
        9 -> 1 tercia ------------------------------ [0,1,0] -------------------- "010" ---------------- 140
        10 -> 2 pares ------------------------------ [0,0,2] -------------------- "002" ---------------- 130
        11 -> 1 par -------------------------------- [0,0,1] -------------------- "001" ---------------- 120
        12 -> Carta más alta ----------------------- [0,0,0] -> No color -------- "000" ---------------- carta.valor
    '''
    # Diccionario con los códigos (key) y el nombre y puntaje de cada posible mano ganadora (value)
    jugadas = {"110": ["poker + 1 tercia", 220], "101": ["poker + 1 par", 210], "100": ["poker",200], "012": ["full + 1 par",190],
               "011": ["full", 180], "CLR": ["color", 170], "020": ["2 tercias", 160], "003": ["3 pares", 150], "010": ["1 tercia",140],
               "002": ["2 pares",130], "001": ["1 par",120], "000": ["Carta más alta", obtener_carta_mayor(jugador.mano)]}
    # Comprobar si la mano es color y, si es así, definir el código como "CLR"
    if (esColor(jugador.mano)):
        codigo = "CLR"
    else:
    # Si la mano no es color, obtener el código utilizando los atributos del jugador
        lista = [len(jugador.poker), len(jugador.tercias), len(jugador.pares)]
        codigo = "".join(str(n) for n in lista)
    # Obtener el nombre de la mano y su puntaje
    nombre_mano, puntaje = jugadas[codigo]
    desempate = obtener_suma_desempate(jugador)
    return nombre_mano, puntaje, desempate

def esColor(mano):
    palos = set(c.palo for c in mano)
    if ( len(palos) == 1):
        return True
    else:
        return False

def obtener_carta_mayor(mano):
    return max(carta.valor for carta in mano)

def obtener_suma_desempate(jugador):
    valor_poker = sum([c.valor for c in jugador.mano if c.simbolo in jugador.poker])
    valor_tercias = sum([c.valor for c in jugador.mano if c.simbolo in jugador.tercias])
    valor_pares = sum([c.valor for c in jugador.mano if c.simbolo in jugador.pares])
    suma = valor_poker + valor_tercias + valor_pares
    return suma

def imagenes_cartas(jugador):
    cartas = {}
    for i,carta in enumerate(jugador.mano):
        key = 'carta{0:d}'.format(i)
        if carta.simbolo is not 'JK':
            cartas[key] = '/static/images/{0}_{1}.png'.format(carta.palo,carta.simbolo)
        else:
            cartas[key] = '/static/images/JK.png'
    return cartas  

def jugar():
    b = cartas.Baraja()
    A = cartas.Jugador("jugador_1")
    B = cartas.Jugador("jugador_2")
    #asignamos cartas a jugador_1 y jugador_2 (eliminando de la baraja las cartas seleccionadas)
    for i in range(0,7):
        A.mano.append(b.cartas.pop())
        B.mano.append(b.cartas.pop())
    #comprobar pares/tercias/poker
    comprobar_manos(A)
    comprobar_manos(B)
    #declarar ganador
    ganador = definir_ganador(A, B)
    return A, B, ganador

def jugar_en_web(A,B):
    cartas_jA = imagenes_cartas(A)
    cartas_jB = imagenes_cartas(B)
    return cartas_jA, cartas_jB

def jugar_web():
    jugador_A, jugador_B, txt_ganador = jugar()
    cartas_A, cartas_B = jugar_en_web(jugador_A, jugador_B)
    return cartas_A, cartas_B, jugador_A, jugador_B, txt_ganador

if __name__ == "__main__":
    main("A","B")

