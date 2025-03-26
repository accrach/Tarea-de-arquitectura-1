def printeo_tablero():
    """
    Esta funcion lo que hace es pedir al usurio el largo del pasillo
    y printea el pasillo corresponfiente.
    """
    Largo = int(input("Largo del pasillo que decea: "))
    i = 0
    #primer while son las columnas.
    while(11>i):
        e = 0
        #segundo while es para las filas.    
        while(Largo> e):
            print("X", end="")
            e+=1
        i+=1    
        print("")

printeo_tablero()
