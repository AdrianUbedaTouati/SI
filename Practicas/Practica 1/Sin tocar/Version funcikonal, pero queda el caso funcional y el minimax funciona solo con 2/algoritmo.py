from tablero import Tablero
from itertools import filterfalse

def InicilizarTableroEvalua():
    global tableroEvalua
    tableroEvalua = Tablero(None)
    for i in range(tableroEvalua.getAncho()):
        for l in range(tableroEvalua.getAlto()):
            if i < 4:
                tableroEvalua.setCelda(l,i, i + l + 1)
            if i == 4:
                tableroEvalua.setCelda(l,i, i + l)
            if i > 4:
                tableroEvalua.setCelda(l,i, l - i + tableroEvalua.getAlto()+1)
        
# busca en col la primera celda vacía
def busca(tablero, col):  
    if tablero.getCelda(0,col) != 0:
        i=-1
    i=0
    while i<tablero.getAlto() and tablero.getCelda(i,col)==0:          
        i=i+1      
    i=i-1
   
    return i

# llama al algoritmo que decide la jugada
def juega(tablero, posicion):
    ####################################################
    ## sustituir este código por la llamada al algoritmo
    coordenadasDisponibles = CoordenadasDisponibles(tablero)
    coordenadasImportantes = CoordenadasImportantes(tablero)
    #print(coordenadas)
    position2 = minimax(tablero,2,True,(0,0),0)
    print("Lo que da al final ", position2)
    
    
    posicion[0] = position2[1][0]
    posicion[1] = position2[1][1]
    
    #coordenadaFinalAtaque = JugadaFinal(tablero,True,coordenadas)
    #print(coordenadaFinalAtaque)
    #coordenadaFinalDefensa = JugadaFinal(tablero,False,coordenadas)
    #print(coordenadaFinalDefensa)
    #coordenadaPeligrosaAtaque = JugadaPeligrosa(tablero,True,coordenadas)
    #print(coordenadaPeligrosaAtaque)
    #coordenadaPeligrosaDefensa = JugadaPeligrosa(tablero,False,coordenadas)
    #print(coordenadaPeligrosaDefensa)
    
    #if coordenadaFinalAtaque[0] != None:
    #    posicion[0]=coordenadaFinalAtaque[0]
    #    posicion[1]=coordenadaFinalAtaque[1]
    #elif coordenadaFinalDefensa[0] != None:
    #    posicion[0]=coordenadaFinalDefensa[0]
    #    posicion[1]=coordenadaFinalDefensa[1]
    #elif coordenadaPeligrosaAtaque[0] != None:
    #    posicion[0]=coordenadaPeligrosaAtaque[0]
    #    posicion[1]=coordenadaPeligrosaAtaque[1]
    #elif coordenadaPeligrosaDefensa[0] != None:
    #    posicion[0]=coordenadaPeligrosaDefensa[0]
    #    posicion[1]=coordenadaPeligrosaDefensa[1]
    
    #f1,c1=PeligroPartida(tablero)
   
    ####################################################
        
def evalua(tablero,coordenadas):
    #Jugadas claves
    cuatroEnRayaAtaque = 100000
    cuatroEnRayaDefensa = -10000
    
    ganador = tablero.cuatroEnRaya()
    if ganador != 0 and ganador == 1:
        return cuatroEnRayaDefensa
    elif ganador == 2:
        return cuatroEnRayaAtaque
    
    jugadaFinalAtaque = 1000
    jugadaFinalDefensa = -100
    
    jugadaPeligrosaAtaque = 50
    jugadaPeligrosaDefensa = -50
    
    intentarFormarAtaque = 20
    
    coordenadaFinalAtaque = JugadaFinal(tablero,True,coordenadas)
    coordenadaFinalDefensa = JugadaFinal(tablero,False,coordenadas)
    coordenadaPeligrosaAtaque = JugadaPeligrosa(tablero,True,coordenadas)
    coordenadaPeligrosaDefensa = JugadaPeligrosa(tablero,False,coordenadas)
    
    resultado = 0
    
    if coordenadaFinalAtaque[0] != None:
        resultado += jugadaFinalAtaque
        #puntuacion.append(jugadaFinalAtaque)
    if coordenadaFinalDefensa[0] != None:
        resultado += jugadaFinalDefensa
        #puntuacion.append(jugadaFinalDefensa)
    if coordenadaPeligrosaAtaque[0] != None:
        resultado += jugadaPeligrosaAtaque
        #puntuacion.append(jugadaPeligrosaAtaque)
    if coordenadaPeligrosaDefensa[0] != None:
        resultado += jugadaPeligrosaDefensa
        #puntuacion.append(jugadaPeligrosaDefensa)
    
    #for puntos in puntuacion:
        #print("Puntuacion ",puntos)
     #   if puntos > resultado:
      #      resultado = puntos
    
    
    #if resultado == -1:
    #    print(Intermedio(tablero))
    
    #Jugadas intermedias
    #if resultado == -1:
    #    coordenadaAtaque = IntentarFormarAtaque(tablero)
    #    print("Funcion ",coordenadaAtaque)
    #    if coordenadaAtaque[0] != None:
    #        resultado = intentarFormarAtaque
    

    return resultado

def CoordenadasDisponibles(tablero):
    coordenadas=[]
    i = -2
    for j in range(tablero.ancho):
        i = busca(tablero,j)
        if i == -1:
            i = 0
        
        coordenadas.append((i,j))
                
    return coordenadas
        
def Intermedio(tablero):
    print(CoordenadasDisponibles(tablero))
    
def PosibleCuatroEnRaya(tablero,coordenada):
    i = coordenada [0]
    j = coordenada [1]
    
    casillaTieneSuelo = 1
    
    posibleCuatroEnRaya = 10
    
    fichaEnRaya = 10000
    
    puntuacion = -1
    
    coordenadas=[(-1,-1),(-1,-1),(-1,-1)]
    
    #"Horizontal"
    #".---"  
    if j < 5:
        coordenadas[0] = (i,j+1)
        coordenadas[1] = (i,j+2)
        coordenadas[2] = (i,j+3)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
            
    #"---."            
    if j > 2:
        coordenadas[0] = (i,j-1)
        coordenadas[1] = (i,j-2)
        coordenadas[2] = (i,j-3)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
        
    #"-.--"            
    if j > 0 and j < 6:
        coordenadas[0] = (i,j-1)
        coordenadas[1] = (i,j+1)
        coordenadas[2] = (i,j+2)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
    
    #"--.-"            
    if j > 1 and j < 7:
        coordenadas[0] = (i,j-1)
        coordenadas[1] = (i,j-2)
        coordenadas[2] = (i,j+1)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
                        
    #"Vertical
    #-
    #-
    #-
    #.
    if i > 2 :
        puntuacion += posibleCuatroEnRayac
    
    #Diagonal derecha
    #   -
    #  -
    # -
    #.
    if j < 5 and i > 2:
        coordenadas[0] = (i+1,j+1)
        coordenadas[1] = (i+2,j+2)
        coordenadas[2] = (i+3,j+3)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
    
    #   -
    #  -
    # .
    #-
    if j < 6 and j > 0 and i > 1 and i < 6:
        coordenadas[0] = (i-1,j-1)
        coordenadas[1] = (i+1,j+1)
        coordenadas[2] = (i+2,j+2)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
        
    #   -
    #  .
    # -
    #-
    if j < 7 and j > 1 and i > 0 and i < 5:
        coordenadas[0] = (i-1,j-1)
        coordenadas[1] = (i-2,j-2)
        coordenadas[2] = (i+1,j+1)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
    
    #   .
    #  -
    # -
    #-
    if j < 4 and i > 0:
        coordenadas[0] = (i-1,j-1)
        coordenadas[1] = (i+1,j+1)
        coordenadas[2] = (i+2,j+2)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
        
    #Diagonal izquierda
    #.   
    # -
    #  -
    #   -
    if j > 5 and i > 2:
        coordenadas[0] = (i+1,j+1)
        coordenadas[1] = (i+2,j+2)
        coordenadas[2] = (i+3,j+3)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
    
    #.   
    # -
    #  -
    #   -
    if j < 6 and j > 0 and i > 1:
        coordenadas[0] = (i-1,j-1)
        coordenadas[1] = (i+1,j+1)
        coordenadas[2] = (i+2,j+2)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
        
    #.   
    # -
    #  -
    #   -
    if j < 7 and j > 1 and i > 0:
        coordenadas[0] = (i-1,j-1)
        coordenadas[1] = (i-2,j-2)
        coordenadas[2] = (i+1,j+1)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
    
    #.   
    # -
    #  -
    #   -
    if j < 4 and i > 0:
        coordenadas[0] = (i-1,j-1)
        coordenadas[1] = (i+1,j+1)
        coordenadas[2] = (i+2,j+2)
        puntuacion += AuxPosibleCuatroEnRaya(coordenadas)
        
def AuxPosibleCuatroEnRaya(tablero,coordenadas):
    casillaTieneSuelo = 1
    
    posibleCuatroEnRaya = 10
    
    fichaEnRaya = 10000
    
    puntuacion = 0
    
    if tablero.getCelda(coordenadas[0]) == (0 or 2) and tablero.getCelda(coordenadas[1]) == (0 or 2) and tablero.getCelda(coordenadas[2]) == (0 or 2):
            if tablero.getCelda(coordenadas[0]) == 2 or tablero.getCelda(coordenadas[1]) == 2 or tablero.getCelda(coordenadas[2]) == 2:
                puntuacion += fichaEnRaya
            if SueloFicha(tablero,coordenadas[0]):
                puntuacion += casillaTieneSuelo
                if SueloFicha(tablero,coordenadas[1]):
                    puntuacion += casillaTieneSuelo
                    if SueloFicha(tablero,coordenadas[2]):
                        puntuacion += casillaTieneSuelo
            puntuacion += posibleCuatroEnRaya
    
    return puntuacion
    
    
def minimax(tablero,n,turno,coordenada,aux):
    resultados = []
    
    if n == 0:
        posicionesObjetivo = CoordenadasImportantes(tablero)
        return (evalua(tablero,posicionesObjetivo),coordenada,aux)
    else:
        if turno:
            #print("Hola soy maxi")
            for j in range(tablero.ancho):
                
                if tablero.cuatroEnRaya():
                    #print("Ollelelelele MAX",coordenada)
                    posicionesObjetivo = CoordenadasImportantes(tablero)
                    return (evalua(tablero,posicionesObjetivo),coordenada,aux)
                
                i = busca(tablero,j)
                
                if i == -1:
                    continue
            
                tableroAux = Tablero(tablero)
                tableroAux.setCelda(i,j,2)
                
                coordenada = (i,j)
                
                resultado = minimax(tableroAux,n-1,False,coordenada,aux+1)
                resultados.append((resultado[0],coordenada,resultado[2]))
                
            #print(resultados)
            resultado = resultados[0]
            #filtrada = list(filterfalse(min(resultados)[0], resultados))
            for puntos in resultados:
                if puntos[2] <= resultado[2]:
                    if puntos[0] > resultado[0]:
                        resultado = puntos
                        
            return resultado
            #print(resultados)
            #return max(resultados)
                #return (max(minimax(tableroAux,n-1,False,coordenada)[0]),coordenada)
        else:
            #print("Hola soy mini")
            for j in range(tablero.ancho):
                
                if tablero.cuatroEnRaya():
                    #print("Ollelelelele Mini",coordenada)
                    posicionesObjetivo = CoordenadasImportantes(tablero)
                    return (evalua(tablero,posicionesObjetivo),coordenada,aux)
                
                i = busca(tablero,j)
                
                if i == -1:
                    continue
            
                tableroAux = Tablero(tablero)
                tableroAux.setCelda(i,j,1)
                
                coordenada = (i,j)
                
                resultado = minimax(tableroAux,n-1,True,coordenada,aux+1)
                resultados.append((resultado[0],coordenada,resultado[2]))
                #return (min(minimax(tableroAux,n-1,True,coordenada)[0]),coordenada)
                #resultados.append((minimax(tableroAux,n-1,True,coordenada,aux+1)[0],coordenada))
                
            #print(resultados)
            resultado = resultados[0]
            #filtrada = list(filterfalse(min(resultados)[0], resultados))
            for puntos in resultados:
                if puntos[2] <= resultado[2]:
                    if puntos[0] < resultado[0]:
                        resultado = puntos
                        
            return resultado
    

def CoordenadasImportantes(tablero):
    coordenadas=[]
    i = -2
    for j in range(tablero.ancho):
        i = busca(tablero,j)
        if i == -1:
            i = 0
        for l in range(i,tablero.alto,1):
            coordenadas.append((l,j))
                
    return coordenadas

    
def JugadaPeligrosa(tablero,ataque,coordenadas):
    jugAnalizado = 0
    if ataque == True:
        jugAnalizado = 2
    else:
        jugAnalizado = 1
        
    i = -1
    j = -1
        
            
    for coordenada in coordenadas:
        i = coordenada[0]
        j = coordenada[1]
        
        #"_._._"
        if j < 4:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == 0 and tablero.getCelda(i,j+3) == jugAnalizado and tablero.getCelda(i,j+4) == 0:
                    if SueloFicha(tablero,(i,j+2)) and SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i,j+4)):
                        return (i,j+2)
        #"_
        #"_.
        #"___
        #"___.
        #"_____      
        if j < 4 and i < 3:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j + 1) == jugAnalizado and tablero.getCelda(i + 2,j + 2) == 0 and tablero.getCelda(i + 3,j + 3) == jugAnalizado and tablero.getCelda(i + 4,j + 4) == 0:
                    if SueloFicha(tablero,(i+2,j+2)) and SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i+4,j+4)):
                        return (i + 2,j + 2)
                        
        #"     _
        #"    ._
        #"   ___
        #" .____
        #"______
        if j < 5 and i < 3:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j - 1) == jugAnalizado and tablero.getCelda(i + 2,j - 2) == 0 and tablero.getCelda(i + 3,j - 3) == jugAnalizado and tablero.getCelda(i + 4,j - 4) == 0:
                    if SueloFicha(tablero,(i+2,j-2)) and SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i+4,j-4)):
                        return (i + 2,j - 2)
             
                        
                        
        #"_.._"
        if j < 5:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == jugAnalizado and tablero.getCelda(i,j+3) == 0:
                    if SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i,j+3)):
                        return (i,j)
            
        #"      _
        #"     __
        #"    .__
        #"  .____
        #" ______
        #"______
        if j < 6 and i < 2:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j - 1) == 0 and tablero.getCelda(i + 2,j - 2) == jugAnalizado and tablero.getCelda(i + 3,j - 3) == jugAnalizado and tablero.getCelda(i + 4,j - 4) == 0 and tablero.getCelda(i + 5,j - 5) == 0:
                    if SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i+1,j-1)) and SueloFicha(tablero,(i+4,j-4)) and SueloFicha(tablero,(i+5,j-5)):
                        return (i + 1,j - 1)
                        
        #"_
        #"__
        #"__.
        #"___.
        #"_____
        #"______      
        if j < 3 and i < 2:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j + 1) == 0 and tablero.getCelda(i + 2,j + 2) == jugAnalizado and tablero.getCelda(i + 3,j + 3) == jugAnalizado and tablero.getCelda(i + 4,j + 4) == 0 and tablero.getCelda(i + 5,j + 5) == 0:
                    if SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i+1,j+1)) and SueloFicha(tablero,(i+4,j+4)) and SueloFicha(tablero,(i+5,j+5)):
                        return (i + 1,j + 1)
            
    return (None,None)

def JugadaFinal(tablero,ataque,coordenadas):
    jugAnalizado = 0
    if ataque == True:
        jugAnalizado = 2
    else:
        jugAnalizado = 1
        
    i = -1
    j = -1
        
            
    for coordenada in coordenadas:
        i = coordenada[0]
        j = coordenada[1]
        
        #"._.."
        if j < 5:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i,j+1) == 0 and tablero.getCelda(i,j+2) == jugAnalizado and tablero.getCelda(i,j+3) == jugAnalizado:
                    if SueloFicha(tablero,(i,j+1)):
                        return (i,j + 1)
                
            #".
            #"_.
            #"___
            #"___.   
        if j < 5 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j + 1) == jugAnalizado and tablero.getCelda(i + 2,j + 2) == 0 and tablero.getCelda(i + 3,j + 3) == jugAnalizado:
                    if SueloFicha(tablero,(i+2,j+2)):
                        return (i + 2,j + 2)
                        
            #"    .
            #"   __
            #" .___
            #".____
        if j > 2 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j - 1) == 0 and tablero.getCelda(i + 2,j - 2) == jugAnalizado and tablero.getCelda(i + 3,j - 3) == jugAnalizado:
                    if SueloFicha(tablero,(i+1,j-1)):
                        return (i + 1,j - 1)
                
            #".._."
        if j < 5:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == 0 and tablero.getCelda(i,j+3) == jugAnalizado:
                    if SueloFicha(tablero,(i,j+2)):
                        return (i,j + 2)
                
            #".
            #"__
            #"__.
            #"___.   
        if j < 5 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j + 1) == 0 and tablero.getCelda(i + 2,j + 2) == jugAnalizado and tablero.getCelda(i + 3,j + 3) == jugAnalizado:
                    if SueloFicha(tablero,(i+1,j+1)):
                        return (i + 1,j + 1)
            #"    .
            #"   ._
            #" ____
            #".____
        if j > 2 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j - 1) == jugAnalizado and tablero.getCelda(i + 2,j - 2) == jugAnalizado and tablero.getCelda(i + 3,j - 3) == jugAnalizado:
                    if SueloFicha(tablero,(i+2,j-2)):
                        return (i + 2,j - 2)
                  
            #"..._"
        if j < 5:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == jugAnalizado and tablero.getCelda(i,j+3) == 0:
                    if SueloFicha(tablero,(i,j+3)):
                        return (i,j + 3)
                            
            #".
            #"_.
            #"__.
            #"____
        if j < 5 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j + 1) == jugAnalizado and tablero.getCelda(i + 2,j + 2) == jugAnalizado and tablero.getCelda(i + 3,j + 3) == 0:
                    if SueloFicha(tablero,(i+3,j+3)):
                        return (i + 3,j + 3)
            #"   _
            #"  ._
            #" .__
            #".___
        if j > 2 and i < 4:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j - 1) == jugAnalizado and tablero.getCelda(i + 2,j - 2) == jugAnalizado and tablero.getCelda(i + 3,j - 3) == jugAnalizado:
                    if SueloFicha(tablero,(i,j)):
                        return (i,j)
                
            #"_..."
        if j < 5:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == jugAnalizado and tablero.getCelda(i,j+3) == jugAnalizado:
                    if SueloFicha(tablero,(i,j)):
                        return (i,j)
                            
            #"_
            #"_.
            #"__.
            #"___.
        if j < 5 and i < 4:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j + 1) == jugAnalizado and tablero.getCelda(i + 2,j + 2) == jugAnalizado and tablero.getCelda(i + 3,j + 3) == jugAnalizado:
                    if SueloFicha(tablero,(i,j)):
                        return (i,j)
            #"    .
            #"   ._
            #" .___
            #"_____
        if j > 2 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j - 1) == jugAnalizado and tablero.getCelda(i + 2,j - 2) == jugAnalizado and tablero.getCelda(i + 3,j - 3) == 0:
                    if SueloFicha(tablero,(i+3,j-3)):
                        return (i+3,j-3)
                            
            #"-
            #". 
            #".
            #".
        if i < 4 :
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i+1,j) == jugAnalizado and tablero.getCelda(i+2,j) == jugAnalizado and tablero.getCelda(i+3,j) == jugAnalizado:
                    if SueloFicha(tablero,(i,j)):
                        return (i,j)
                        
    return (None,None)

def SueloFicha(tablero,coordenada):
    i = coordenada [0]
    j = coordenada [1]
    if i != 6:
        if tablero.getCelda(i+1,j) == 0:
            return False

    return True

"""
else:
        enc=False
        c=0
        while not enc and c<tablero.getAncho():
            
            f=busca(tablero, c)
            if f!=-1:
                enc=True
            else:
                c=c+1
        if f!=-1:
            posicion[0]=f
            posicion[1]=c
            
def PeligroPartida(tablero):
    for i in range(tablero.alto):
        for j in range(tablero.ancho):
            #"_._._"
            if j < 4:
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i,j+1) == 1 and tablero.getCelda(i,j+2) == 0 and tablero.getCelda(i,j+3) == 1 and tablero.getCelda(i,j+4) == 0:
                        if SueloFicha(tablero,i,j+2) and SueloFicha(tablero,i,j) and SueloFicha(tablero,i,j+4):
                            return (i,j+2)
            #"_
            #"_.
            #"___
            #"___.
            #"_____      
            if j < 4 and i < 3:
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i + 1,j + 1) == 1 and tablero.getCelda(i + 2,j + 2) == 0 and tablero.getCelda(i + 3,j + 3) == 1 and tablero.getCelda(i + 4,j + 4) == 0:
                        if SueloFicha(tablero,i+2,j+2) and SueloFicha(tablero,i,j) and SueloFicha(tablero,i+4,j+4):
                            return (i + 2,j + 2)
                        
            #"     _
            #"    ._
            #"   ___
            #" .____
            #"______
            if j < 4 and i > 3:
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i - 1,j + 1) == 1 and tablero.getCelda(i - 2,j + 2) == 0 and tablero.getCelda(i - 3,j + 3) == 1 and tablero.getCelda(i - 4,j + 4) == 0:
                        if SueloFicha(tablero,i-2,j+2) and SueloFicha(tablero,i,j) and SueloFicha(tablero,i-4,j+4):
                            return (i - 2,j + 2)
            #4 en rayas casi
            #"._.."
            if j < 5:
                if tablero.getCelda(i,j) == 1:
                    if tablero.getCelda(i,j+1) == 0 and tablero.getCelda(i,j+2) == 1 and tablero.getCelda(i,j+3) == 1:
                        if SueloFicha(tablero,i,j+1):
                            return (i,j + 1)
            
            #".
            #"_.
            #"___
            #"___.   
            if j < 5 and i < 4:
                if tablero.getCelda(i,j) == 1:
                    if tablero.getCelda(i + 1,j + 1) == 1 and tablero.getCelda(i + 2,j + 2) == 0 and tablero.getCelda(i + 3,j + 3) == 1:
                        if SueloFicha(tablero,i+2,j+2):
                            return (i + 2,j + 2)
                    
            #"    .
            #"   __
            #" .___
            #".____
            if j < 5 and i > 2:
                if tablero.getCelda(i,j) == 1:
                    if tablero.getCelda(i - 1,j + 1) == 1 and tablero.getCelda(i - 2,j + 2) == 0 and tablero.getCelda(i - 3,j + 3) == 1:
                        if SueloFicha(tablero,i-2,j+2):
                            return (i - 2,j + 2)
                    
            #".._."
            if j < 5:
                if tablero.getCelda(i,j) == 1:
                    if tablero.getCelda(i,j+1) == 1 and tablero.getCelda(i,j+2) == 0 and tablero.getCelda(i,j+3) == 1:
                        if SueloFicha(tablero,i,j+2):
                            return (i,j + 2)
            
            #".
            #"__
            #"__.
            #"___.   
            if j < 5 and i < 4:
                if tablero.getCelda(i,j) == 1:
                    if tablero.getCelda(i + 1,j + 1) == 0 and tablero.getCelda(i + 2,j + 2) == 1 and tablero.getCelda(i + 3,j + 3) == 1:
                        if SueloFicha(tablero,i+1,j+1):
                            return (i + 1,j + 1)
            #"    .
            #"   ._
            #" ____
            #".____
            if j < 5 and i > 2:
                if tablero.getCelda(i,j) == 1:
                    if tablero.getCelda(i - 1,j + 1) == 0 and tablero.getCelda(i - 2,j + 2) == 1 and tablero.getCelda(i - 3,j + 3) == 1:
                        if SueloFicha(tablero,i-1,j+1):
                            return (i - 1,j + 1)
            
            
            #"..._"
            if j < 5:
                if tablero.getCelda(i,j) == 1:
                    if tablero.getCelda(i,j+1) == 1 and tablero.getCelda(i,j+2) == 1 and tablero.getCelda(i,j+3) == 0:
                        if SueloFicha(tablero,i,j+3):
                            return (i,j + 3)
                        
            #".
            #"_.
            #"__.
            #"____
            if j < 5 and i < 4:
                if tablero.getCelda(i,j) == 1:
                    if tablero.getCelda(i + 1,j + 1) == 1 and tablero.getCelda(i + 2,j + 2) == 1 and tablero.getCelda(i + 3,j + 3) == 0:
                        if SueloFicha(tablero,i+3,j+3):
                            return (i + 3,j + 3)
            #"   _
            #"  ._
            #" .__
            #".___
            if j < 5 and i > 2:
                if tablero.getCelda(i,j) == 1:
                    if tablero.getCelda(i - 1,j + 1) == 1 and tablero.getCelda(i - 2,j + 2) == 1 and tablero.getCelda(i - 3,j + 3) == 0:
                        if SueloFicha(tablero,i-3,j+3):
                            return (i - 3,j + 3)
            
            #"_..."
            if j < 5:
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i,j+1) == 1 and tablero.getCelda(i,j+2) == 1 and tablero.getCelda(i,j+3) == 1:
                        if SueloFicha(tablero,i,j):
                            return (i,j)
                        
            #"_
            #"_.
            #"__.
            #"___.
            if j < 5 and i < 4:
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i + 1,j + 1) == 1 and tablero.getCelda(i + 2,j + 2) == 1 and tablero.getCelda(i + 3,j + 3) == 1:
                        if SueloFicha(tablero,i,j):
                            return (i,j)
            #"    .
            #"   ._
            #" .___
            #"_____
            if j < 5 and i > 2:
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i - 1,j + 1) == 1 and tablero.getCelda(i - 2,j + 2) == 1 and tablero.getCelda(i - 3,j + 3) == 1:
                        if SueloFicha(tablero,i,j):
                            return (i,j)
                        
            #"-
            #". 
            #".
            #".
            if i < 4 :
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i+1,j) == 1 and tablero.getCelda(i+2,j) == 1 and tablero.getCelda(i+3,j) == 1:
                        if SueloFicha(tablero,i,j):
                            return (i,j)
                        
            #"_.._"
            if j < 5:
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i,j+1) == 1 and tablero.getCelda(i,j+2) == 1 and tablero.getCelda(i,j+3) == 0:
                        if SueloFicha(tablero,i,j) and SueloFicha(tablero,i,j+3):
                            return (i,j)
                        
            #"      _
            #"     __
            #"    .__
            #"  .____
            #" ______
            #"______
            if j < 3 and i > 4:
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i - 1,j + 1) == 0 and tablero.getCelda(i - 2,j + 2) == 1 and tablero.getCelda(i - 3,j + 3) == 1 and tablero.getCelda(i - 4,j + 4) == 0 and tablero.getCelda(i - 5,j + 5) == 0:
                        if SueloFicha(tablero,i,j) and SueloFicha(tablero,i-1,j+1) and SueloFicha(tablero,i-4,j+4) and SueloFicha(tablero,i-5,j+5):
                            return (i - 1,j + 1)
                        
            #"_
            #"__
            #"__.
            #"___.
            #"_____
            #"______      
            if j < 3 and i < 2:
                if tablero.getCelda(i,j) == 0:
                    if tablero.getCelda(i + 1,j + 1) == 0 and tablero.getCelda(i + 2,j + 2) == 1 and tablero.getCelda(i + 3,j + 3) == 1 and tablero.getCelda(i + 4,j + 4) == 0 and tablero.getCelda(i + 5,j + 5) == 0:
                        if SueloFicha(tablero,i,j) and SueloFicha(tablero,i+1,j+1) and SueloFicha(tablero,i+4,j+4) and SueloFicha(tablero,i+5,j+5):
                            return (i + 1,j + 1)
            
    return (None,None)
    
    
def AdjacenciaCasilla(tablero,coordenada):
    casillasAdjacentes = []
    x = coordenada[0]
    y = coordenada[1]
    
    if y == 6:
        casillasAdjacentes.append(coordenada(x,y-1))
    elif y == 0:
        casillasAdjacentes.append(coordenada(x,y+1))
    else:
        casillasAdjacentes.append(coordenada(x,y+1))
        casillasAdjacentes.append(coordenada(x,y-1))
    
    if x == 
   

def IntentarFormarAtaque(tablero):
    
    i = -2
    for j in range(tablero.ancho):
        i = busca(tablero,j)
        
        if i == -1:
            continue
            
        tableroAux = Tablero(tablero)
        tableroAux.setCelda(i,j,2)
        
        print(tableroAux)
        
        coordenadaPeligrosaAtaque = JugadaPeligrosa(tableroAux,True,CoordenadasImportantes(tableroAux))
        
        if coordenadaPeligrosaAtaque[0] != None:
            return coordenadaPeligrosaAtaque
    
    return None,None
    
    if position2[0] == 0:
        enc=False
        c=0
        while not enc and c<tablero.getAncho():
            f=busca(tablero, c)
            if f!=-1:
                enc=True
            else:
                c=c+1
        if f!=-1:
            posicion[0]=f
            posicion[1]=c
    else:
"""


                            
                