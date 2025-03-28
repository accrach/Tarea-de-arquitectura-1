import random
import math

def binario(numero_binario):
    
    posicion = len(numero_binario) -1
    
    for i in numero_binario:
        digito = int(i)
        print(digito, 'posicion: ', posicion)
        print(digito ** posicion)
        posicion -= 1
       


def Mover_personaje(Matriz,Largo):
    """
    Esta funcion lo que hace es simplemente preguntar a donde se quiere mover
    y cambiar los valores de la matriz.
    Matriz: es el tablero con la informacion actual de tablero.
    Largo: es el largo del tablero
    """
    print("¿Para donde te quieres mover?")
    print("W: Moverse hacia arriba")
    print("S: Moverse hacia abajo")
    print("A: Moverse hacia la izquierda")
    print("D: Moverse hacia la derecha")
    
    R = ''
    while(R != 'W' and R != 'S' and R != 'A' and R != 'D' ): #para que solo pueda ingresar un movimiento valido por consola
    
        R = input("Ingrese respuesta: ").upper() #Guardamos las respuestas simepre en mayusculas aunque el usuario ingrese minusculas
    

        movimiento = ''                          #Para despues imprimir en consola hacia donde selecciono moverse
        if(R == 'W'):
            movimiento = "arriba"
        elif(R == 'S'):
            movimiento = "abajo"
        elif(R == 'A'):
            movimiento == "la izquierda"
        elif(R == 'D'):
            movimiento == "la derecha"
        else:
            print("Movimiento inexistente")


    if(Largo<20):
        print("Debe de ingresar la cantidad de casillas que se quiere mover hacia", movimiento, "en formato binario")
        numero_binario = input("Ingrese cantidad:")
        binario(numero_binario)

    elif(Largo<100):    
        print("Debe de ingresar la cantidad de casillas que se quiere mover hacia", movimiento, "en octal")
        numero_octal = int(input("Ingrese cantidad:"))

    else:
        print("Debe de ingresar la cantidad de casillas que se quiere mover hacia", movimiento, "en hexadecimal")    
        numero_hexadecimal = int(input("Ingrese cantidad:"))

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

    return (Tablero,Largo)

Largo_pasillo = 0
# Llamar a la función
tablero,Largo_pasillo = creacion_tablero()
Imprimir_tablero(tablero)
# print(Largo_pasillo)
Mover_personaje(tablero, Largo_pasillo)