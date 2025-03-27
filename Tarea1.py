import random

def printeo_tablero():
    """
    Esta funcion lo que hace es pedir al usurio el largo del pasillo
    y printea el pasillo corresponfiente.
    """
    Largo = int(input("Largo del pasillo que desea: "))
    guardias = int(input("Ingrese cantidad de guardias que desea: "))

    posiciones_guardias = random.sample(range(11 * Largo), guardias)
    cant_guardias_printed = 0
    i = 0
    contador = 0
    #primer while son las columnas.
    while(11>i):
        e = 0
        #segundo while es para las filas.    
        while(Largo> e):
            if e == 0 and i == 5:
                print("S", end="")
            
            elif cant_guardias_printed < guardias and contador in posiciones_guardias:
                print("!", end="")
                cant_guardias_printed += 1
            else:
                print("X", end="")
            e+=1
            contador += 1
        i+=1    
        print("")

printeo_tablero()
