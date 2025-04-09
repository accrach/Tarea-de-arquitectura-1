import random
import math

def binario(numero_binario):     #retorna el valor en decimal del numero binario ingresado
    
    posicion = len(numero_binario) - 1
    total = 0
    for i in numero_binario:
        digito = int(i)
        if digito == 1:
            valor = 2 ** posicion
            total += valor 
        posicion -= 1
    return total

def octal(numero_octal):            #retorna el valor en decimal del numero octal ingresado
    posicion = len(numero_octal) - 1
    total = 0

    for i in numero_octal:
        digito = int(i)
        valor = (8 ** posicion) * digito
        posicion -= 1
        total += valor
    return total 

def hexadecimal(numero_hexadecimal):     #retorna el valor en decimal del numero hexadecimal ingresado
    
    posicion = len(numero_hexadecimal) - 1
    total = 0
    numero_hexadecimal = numero_hexadecimal.upper()
    for i in numero_hexadecimal:
        if i.isdigit():
            valor = (16 ** posicion) * int(i) 
            total += valor
        
        else:
            if i == 'A':
                valor = (16 ** posicion) * 10
                total += valor
            elif i == 'B':
                valor = (16 ** posicion) * 11
                total += valor
            elif i == 'C':
                valor = (16 ** posicion) * 12
                total += valor
            elif i == 'D':
                valor = (16 ** posicion) * 13
                total += valor
            elif i == 'E':
                valor = (16 ** posicion) * 14
                total += valor
            elif i == 'F':
                valor = (16 ** posicion) * 15
                total += valor

        posicion -= 1
    
    return total


def decimal_to_bin(numero):
    num_bin = ''
    while numero > 0:
        resto = numero%2
        num_bin = str(resto) + num_bin
        numero = numero//2
    return int(num_bin)

def decimal_to_oct(numero):
    num_oct = ''
    while numero > 0:
        resto = numero%8
        num_oct = str(resto) + num_oct
        numero = numero//8
    return int(num_oct)

def decimal_to_hex(numero):
    num_hex = ''
    while numero > 0:
        resto = numero%16
        if resto < 10:
            num_hex = str(resto) + num_hex

        elif(resto == 10):
            print('s')
            num_hex = 'A' + num_hex

        elif(resto == 11):
            num_hex = 'B' + num_hex

        elif(resto == 12):
            num_hex = 'C' + num_hex

        elif(resto == 13):
            num_hex = 'D' + num_hex

        elif(resto == 14):
            num_hex = 'E' + num_hex
        
        elif(resto == 15):
            num_hex = 'F' + num_hex
        
        numero = numero//16
    
    return num_hex


def hackeo(largo):
    numero = random.randint(0, 10000)
    if largo <= 20:
        num_bin = decimal_to_bin(numero)
        respuesta = input("El numero en binario " + str(num_bin) + " es igual a: " )
        if(int(respuesta) == numero):
            return True
        else:
            return False
    
    elif largo <= 100:
        num_oct = decimal_to_oct(numero)
        respuesta = input("El numero en octal " + str(num_oct) + " es igual a: " )
        if(int(respuesta) == numero):
            return True
        else:
            return False

    else:
        num_hex = decimal_to_hex(numero)
        respuesta = input("El numero en hexadecimal " + str(num_hex) + " es igual a: " )
        if(respuesta == str(numero)):
            return True
        else:
            return False
    


def movimiento_snake(Matriz, pos_snake, pasos, R, estado):
    # print(pos_snake)
    x, y = pos_snake
    filas = len(Matriz)
    columnas = len(Matriz[0])
    Matriz[y][x] = "X"

    posiciones_intermedias = []     #para ir viendo si de camino se topa un guardia o la meta

    for i in range(pasos):
        nuevo_x = x
        nuevo_y = y


        if(R == 'W'):
            nuevo_y -= 1
        elif(R == 'S'):
            nuevo_y += 1
        elif(R == 'A'):
            nuevo_x -= 1
        elif(R == 'D'):
            nuevo_x += 1
        
        if (0 <= nuevo_y < len(Matriz) - 1 and 0 <= nuevo_x <= len(Matriz[0]) - 1):
            x, y = nuevo_x, nuevo_y
        
        if (x, y) not in posiciones_intermedias: #va guardando por todas las posiciones que pasa para ver si pasa por encima de un guardia o la meta
            posiciones_intermedias.append((x, y))  #el if para no guardar la posicion repetida y asi el siguiente for itera menos

    for x, y in posiciones_intermedias:
        if Matriz[y][x] == "!":
            estado = 0
            Matriz[y][x] = "S"
            return (False,Matriz, estado)
        elif Matriz[y][x] == "*":
            estado = 1
            Matriz[y][x] = "S"
            return (False,Matriz, estado)
    Matriz[y][x] = "S"
    return (True, Matriz, estado)

def Mover_personaje(Matriz,Largo,estado):
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

    posiciones_guardias = []
    contador_y = 0
    contador_x = 0
    for y in Matriz:
        contador_x = 0
        for x in y:
            if Matriz[contador_y][contador_x] == '*':
                pos_asterisco = (contador_x, contador_y)
            elif Matriz[contador_y][contador_x] == '!':
                posiciones_guardias.append((contador_x, contador_y))
            contador_x += 1
        contador_y += 1
    
    contador_y = 0
    contador_x = 0
    for y in Matriz:
        contador_x = 0
        for x in y:
            if Matriz[contador_y][contador_x] == 'S':
                pos_snake = (contador_x, contador_y)
            
            contador_x += 1
        contador_y += 1


    R = ''
    while(R != 'W' and R != 'S' and R != 'A' and R != 'D' ): #para que solo pueda ingresar un movimiento valido por consola
    
        R = input("Ingrese respuesta: ").upper() #Guardamos las respuestas simepre en mayusculas aunque el usuario ingrese minusculas
    

        movimiento = ''                          #Para despues imprimir en consola hacia donde selecciono moverse
        if(R == 'W'):
            movimiento = "arriba"
        elif(R == 'S'):
            movimiento = "abajo"
        elif(R == 'A'):
            movimiento = "la izquierda"
        elif(R == 'D'):
            movimiento = "la derecha"
        else:
            print("Movimiento inexistente")


    if(Largo<=20):
        print("Debe de ingresar la cantidad de casillas que se quiere mover hacia", movimiento, "en formato binario")
        numero_binario = input("Ingrese cantidad:")
        pasos = binario(numero_binario)
        return movimiento_snake(Matriz, pos_snake, pasos, R, estado)
        

    elif(Largo<=100):    
        print("Debe de ingresar la cantidad de casillas que se quiere mover hacia", movimiento, "en octal")
        numero_octal = input("Ingrese cantidad:")
        pasos = octal(numero_octal)
        return movimiento_snake(Matriz, pos_snake, pasos, R, estado)

    else:
        print("Debe de ingresar la cantidad de casillas que se quiere mover hacia", movimiento, "en hexadecimal")    
        numero_hexadecimal = input("Ingrese cantidad:")
        pasos = hexadecimal(numero_hexadecimal)
        return movimiento_snake(Matriz, pos_snake, pasos, R, estado)

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
I = True
estado = 0
while(I):
    I, tablero, estado = Mover_personaje(tablero, Largo_pasillo, estado)
    Imprimir_tablero(tablero)

if(estado == 1):
    ganador = hackeo(Largo_pasillo)

if ganador:
    print("Felicitaciones, has ganado\n")
else:
    print("Lo lamento, has perdido")
