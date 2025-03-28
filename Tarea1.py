import random

def Imprimir_tablero(Tablero):

    """
    Esta funcion lo que hace es simplemente imprimir el tablero (la matriz con la informacion).
    Tablero: Matriz que imprimira.
    """
    for fila in Tablero:
            print(" ".join(fila))

def creacion_tablero():
    """
    Crea una matriz que representa el pasillo con:
    - 'S' para el jugador
    - 'X' para espacios vacíos
    - '!' para guardias en posiciones aleatorias
    - '*' para el objetivo del juego
    Retorna la matriz que es la informacion de nuestro tablero
    """
    Largo = int(input("Largo del pasillo que desea: "))
    guardias = int(input("Ingrese cantidad de guardias que desea: "))

    pos_objetivo = random.randint(0,10)
    posiciones_guardias = random.sample(range(11 * Largo), guardias)
    cant_guardias_printed = 0
    contador = 0
    Tablero = []

    # Primer while: Itera sobre las filas (11 filas)
    i = 0
    while i < 11:
        Fila = []  # Se crea la fila correctamente
        e = 0

        # Segundo while: Itera sobre las columnas (Largo del pasillo)
        while e < Largo:
            if e == 0 and i == 5:
                Fila.append("S")  # Coloca el jugador
            elif cant_guardias_printed < guardias and contador in posiciones_guardias:
                Fila.append("!")  # Coloca un guardia
                cant_guardias_printed += 1
            else:
                Fila.append("X")  # Espacios vacíos
            
            e += 1
            contador += 1
        
        Tablero.append(Fila)  # Agregar la fila completa a la matriz
        i += 1
    Tablero[pos_objetivo].pop()
    Tablero[pos_objetivo].append("*")

    return Tablero

# Llamar a la función
tablero = creacion_tablero()
Imprimir_tablero(tablero)


