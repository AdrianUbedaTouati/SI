from tablero import Tablero
from itertools import filterfalse
import random

tableroEvalua = Tablero(None)
tableroPrueba = Tablero(None)
tableroConteo = Tablero(None)

def InicilizarTableroEvalua():
    global tableroEvalua 
    for i in range(tableroEvalua.getAncho()):
        for l in range(tableroEvalua.getAlto()):
            if i < 4:
                tableroEvalua.setCelda(l,i, i + l + 1)
            if i == 4:
                tableroEvalua.setCelda(l,i, i + l)
            if i > 4:
                tableroEvalua.setCelda(l,i, l - i + tableroEvalua.getAlto()+1)
def CreacionMatriz():
    global tableroPrueba 
    for i in range(tableroPrueba.getAncho()):
        for l in range(tableroPrueba.getAlto()):
            tableroPrueba.setCelda(l,i,2)
            
def TableroVacio(tablero):
    count = 0 
    for i in range(tablero.getAncho()):
        for l in range(tablero.getAlto()):
            if tableroPrueba.getCelda(l,i)!= 0:
                count += 1
            if count >1:
                return False
    return True

def TableroLleno(tablero):
    count = 0 

    for l in range(tablero.getAncho()):
        if tablero.getCelda(0,l) == 1 or tablero.getCelda(0,l)== 2 :
            count += 1
        else:
            break
        if count == 8:
            return True
    return False
            
def MatrizEvalua():
    CreacionMatriz()
    global tableroConteo
    global tableroPrueba
    for i in range(tableroPrueba.getAlto()):
        for j in range(tableroPrueba.getAncho()):
            casilla=tableroPrueba.getCelda(i,j)
            #búsqueda en horizontal
            if (j+3) <tableroPrueba.getAncho():
                if tableroPrueba.getCelda(i, j+1)==casilla and tableroPrueba.getCelda(i, j+2)==casilla and tableroPrueba.getCelda(i, j+3)==casilla:
                    tableroConteo.setCelda(i,j,tableroConteo.getCelda(i,j)+1)
                    tableroConteo.setCelda(i,j+1,tableroConteo.getCelda(i,j+1)+1)
                    tableroConteo.setCelda(i,j+2,tableroConteo.getCelda(i,j+2)+1)
                    tableroConteo.setCelda(i,j+3,tableroConteo.getCelda(i,j+3)+1)                
                            
            #búsqueda en vertical
            if (i+3) <tableroPrueba.getAlto():
                if tableroPrueba.getCelda(i+1, j)==casilla and tableroPrueba.getCelda(i+2, j)==casilla and tableroPrueba.getCelda(i+3, j)==casilla:
                    tableroConteo.setCelda(i,j,tableroConteo.getCelda(i,j)+1)
                    tableroConteo.setCelda(i+1,j,tableroConteo.getCelda(i+1,j)+1)
                    tableroConteo.setCelda(i+2,j,tableroConteo.getCelda(i+2,j)+1)
                    tableroConteo.setCelda(i+3,j,tableroConteo.getCelda(i+3,j)+1)
                            
            #búsqueda en diagonal
            if (i+3) <tableroPrueba.getAlto():
                if (j-3) >= 0:
                    if tableroPrueba.getCelda(i+1, j-1)==casilla and tableroPrueba.getCelda(i+2, j-2)==casilla and tableroPrueba.getCelda(i+3, j-3)==casilla:
                        tableroConteo.setCelda(i,j,tableroConteo.getCelda(i,j)+1)
                        tableroConteo.setCelda(i+1,j-1,tableroConteo.getCelda(i+1,j-1)+1)
                        tableroConteo.setCelda(i+2,j-2,tableroConteo.getCelda(i+2,j-2)+1)
                        tableroConteo.setCelda(i+3,j-3,tableroConteo.getCelda(i+3,j-3)+1)
                if (j+3) <tableroPrueba.getAncho():
                    if tableroPrueba.getCelda(i+1, j+1)==casilla and tableroPrueba.getCelda(i+2, j+2)==casilla and tableroPrueba.getCelda(i+3, j+3)==casilla:
                        tableroConteo.setCelda(i,j,tableroConteo.getCelda(i,j)+1)
                        tableroConteo.setCelda(i+1,j+1,tableroConteo.getCelda(i+1,j+1)+1)
                        tableroConteo.setCelda(i+2,j+2,tableroConteo.getCelda(i+2,j+2)+1)
                        tableroConteo.setCelda(i+3,j+3,tableroConteo.getCelda(i+3,j+3)+1)
                                
    print(tableroConteo)
    print(tableroPrueba)

        
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
    if TableroVacio(tablero):
        InicilizarTableroEvalua()
        MatrizEvalua()
    
    coordenadasDisponibles = CoordenadasDisponibles(tablero)
    coordenadasImportantes = CoordenadasImportantes(tablero)
    #print(coordenadas)
    #position2 = minimax(tablero,4,True,(0,0),0)
    position2 = alfabeta(tablero,4,True,(0,0),0,-100000000000,10000000000000)
    print("Lo que da al final ", position2)
    
    posicion[0] = position2[1][0]
    posicion[1] = position2[1][1]
        
def evalua(tablero,coordenadas):
    resultado = 0
    
    cuatroEnRayaAtaque = 100000
    cuatroEnRayaDefensa = -100000
    
    ganador = tablero.cuatroEnRaya()
    if ganador != 0 and ganador == 1:
        resultado += cuatroEnRayaDefensa
    elif ganador == 2:
        resultado += cuatroEnRayaAtaque
    
    jugadaFinalAtaque = 1000
    jugadaFinalDefensa = -1000
    
    jugadaPeligrosaAtaque = 100
    jugadaPeligrosaDefensa = -100
    
    
    
    resultado += jugadaFinalAtaque *JugadaFinal(tablero,True,coordenadas)
    resultado += jugadaFinalDefensa * JugadaFinal(tablero,False,coordenadas)
    resultado += jugadaPeligrosaAtaque * JugadaPeligrosa(tablero,True,coordenadas)
    resultado += jugadaPeligrosaDefensa * JugadaPeligrosa(tablero,False,coordenadas)
    
    #Jugadas intermedias
    resultado += PosibleCuatroEnRaya(tablero,coordenadas)
    
    resultado += Intermedio(tablero,coordenadas)
    
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
        
def Intermedio(tablero,coordenadas):
    puntuacion = 0
    global tableroConteo 
    for cordenada in coordenadas:
        if tablero.getCelda(cordenada[0],cordenada[1]) == 1:
            puntuacion -= tableroConteo.getCelda(cordenada[0],cordenada[1])
        if tablero.getCelda(cordenada[0],cordenada[1]) == 2:
            puntuacion += tableroConteo.getCelda(cordenada[0],cordenada[1])
            
    return puntuacion
    
def PosibleCuatroEnRaya(tablero,coordenadas):
    
    for coordenada in coordenadas:
        i = coordenada [0]
        j = coordenada [1]
        
        casillaTieneSuelo = 1
        
        posibleCuatroEnRaya = 2
        
        fichaEnRaya = 5
        
        puntuacion = 0
        
        coordenadasAux=[(-1,-1),(-1,-1),(-1,-1)]
        
        #"Horizontal"
        #".---"  
        if j < 5:
            coordenadasAux[0] = (i,j+1)
            coordenadasAux[1] = (i,j+2)
            coordenadasAux[2] = (i,j+3)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
                
        #"---."            
        if j > 2:
            coordenadasAux[0] = (i,j-1)
            coordenadasAux[1] = (i,j-2)
            coordenadasAux[2] = (i,j-3)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
            
        #"-.--"            
        if j > 0 and j < 6:
            coordenadasAux[0] = (i,j-1)
            coordenadasAux[1] = (i,j+1)
            coordenadasAux[2] = (i,j+2)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
        
        #"--.-"            
        if j > 1 and j < 7:
            coordenadasAux[0] = (i,j-1)
            coordenadasAux[1] = (i,j-2)
            coordenadasAux[2] = (i,j+1)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
                            
        #"Vertical
        #-
        #-
        #-
        #.
        if i > 2 :
            puntuacion += posibleCuatroEnRaya
        
        #Diagonal derecha
        #   -
        #  -
        # -
        #.
        if j < 5 and i > 2:
            coordenadasAux[0] = (i-1,j+1)
            coordenadasAux[1] = (i-2,j+2)
            coordenadasAux[2] = (i-3,j+3)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
        
        #   -
        #  -
        # .
        #-
        if j < 6 and j > 0 and i > 1 and i < 6:
            coordenadasAux[0] = (i+1,j-1)
            coordenadasAux[1] = (i-1,j+1)
            coordenadasAux[2] = (i-2,j+2)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
            
        #   -
        #  .
        # -
        #-
        if j < 7 and j > 1 and i > 0 and i < 5:
            coordenadasAux[0] = (i-1,j+1)
            coordenadasAux[2] = (i+1,j-1)
            coordenadasAux[1] = (i+2,j-2)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
        
        #   .
        #  -
        # -
        #-
        if j > 3 and i < 4:
            coordenadasAux[0] = (i+1,j-1)
            coordenadasAux[1] = (i+2,j-2)
            coordenadasAux[2] = (i+3,j-3)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
            
        #Diagonal izquierda
        #.   
        # -
        #  -
        #   -
        if j < 5 and i < 4:
            coordenadasAux[0] = (i+1,j+1)
            coordenadasAux[1] = (i+2,j+2)
            coordenadasAux[2] = (i+3,j+3)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
        
        #-  
        # .
        #  -
        #   -
        if j < 6 and j > 0 and i > 0 and i < 5:
            coordenadasAux[0] = (i-1,j-1)
            coordenadasAux[1] = (i+1,j+1)
            coordenadasAux[2] = (i+2,j+2)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
            
        #-  
        # -
        #  .
        #   -
        if j < 7 and j > 1 and i > 1 and i < 6:
            coordenadasAux[0] = (i-1,j-1)
            coordenadasAux[1] = (i+1,j+1)
            coordenadasAux[2] = (i-2,j-2)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
        
        #-   
        # -
        #  -
        #   .
        if j > 2 and i > 2:
            coordenadasAux[0] = (i-1,j-1)
            coordenadasAux[1] = (i-2,j-2)
            coordenadasAux[2] = (i-3,j-3)
            puntuacion += AuxPosibleCuatroEnRaya(tablero,coordenadasAux)
    
    return puntuacion
        
def AuxPosibleCuatroEnRaya(tablero,coordenadas):
    casillaTieneSuelo = 1
    
    posibleCuatroEnRaya = 2
    
    fichaEnRaya = 5
    
    puntuacion = 0
    
    coordenada0 = coordenadas[0]
    coordenada1 = coordenadas[1]
    coordenada2 = coordenadas[2]
    
    if tablero.getCelda(coordenada0[0],coordenada0[1]) == (0 or 2) and tablero.getCelda(coordenada1[0],coordenada1[1]) == (0 or 2) and tablero.getCelda(coordenada2[0],coordenada2[1]) == (0 or 2):
            if tablero.getCelda(coordenada0[0],coordenada0[1]) == 2 or tablero.getCelda(coordenada1[0],coordenada1[1]) == 2 or tablero.getCelda(coordenada2[0],coordenada2[1]) == 2:
                puntuacion += fichaEnRaya
            if SueloFicha(tablero,coordenada0):
                puntuacion += casillaTieneSuelo
                if SueloFicha(tablero,coordenada1):
                    puntuacion += casillaTieneSuelo
                    if SueloFicha(tablero,coordenada2):
                        puntuacion += casillaTieneSuelo
            puntuacion += posibleCuatroEnRaya
            
    if tablero.getCelda(coordenada0[0],coordenada0[1]) == (0 or 1) and tablero.getCelda(coordenada1[0],coordenada1[1]) == (0 or 1) and tablero.getCelda(coordenada2[0],coordenada2[1]) == (0 or 1):
            if tablero.getCelda(coordenada0[0],coordenada0[1]) == 1 or tablero.getCelda(coordenada1[0],coordenada1[1]) == 1 or tablero.getCelda(coordenada2[0],coordenada2[1]) == 1:
                puntuacion -= fichaEnRaya
            if SueloFicha(tablero,coordenada0):
                puntuacion -= casillaTieneSuelo
                if SueloFicha(tablero,coordenada1):
                    puntuacion -= casillaTieneSuelo
                    if SueloFicha(tablero,coordenada2):
                        puntuacion -= casillaTieneSuelo
            puntuacion -= posibleCuatroEnRaya
    
    return puntuacion

def alfabeta(tablero,n,turno,coordenada,aux,alfa,beta):
    resultados = []
    
    if n == 0 or tablero.cuatroEnRaya():
        posicionesObjetivo = CoordenadasImportantes(tablero)
        return (evalua(tablero,posicionesObjetivo),coordenada,aux)
    else:
        if turno:
            for j in range(tablero.ancho):
                
                i = busca(tablero,j)
                
                if i == -1:
                    continue
            
                tableroAux = Tablero(tablero)
                tableroAux.setCelda(i,j,2)
                
                coordenada = (i,j)
                #beta es el que da el fallo alfa siempre da el buen valor
                resultado = alfabeta(tableroAux,n-1,False,coordenada,aux+1,alfa,beta)
                if resultado != None:
                    resultados.append((resultado[0],coordenada,resultado[2]))
                    if resultado[0] > alfa:
                        alfa = resultado[0]
                        if alfa >= beta:
                            break
            
            if len(resultados) != 0:
                resultado = resultados[0]
                for puntos in resultados:
                    if puntos[0] > resultado[0]:
                        if puntos[0] > 80000 and resultado[0] > 80000:
                            if resultado[2] > puntos[2]:
                                resultado = puntos
                        else:
                            resultado = puntos
                    elif puntos[0] == resultado[0] and resultado[2] > puntos[2]:
                        resultado = puntos
                    
                            
                return resultado
            else:
                return None
            
        else:
            for j in range(tablero.ancho):
                
                i = busca(tablero,j)
                
                if i == -1:
                    continue
            
                tableroAux = Tablero(tablero)
                tableroAux.setCelda(i,j,1)
                
                coordenada = (i,j)
                
                resultado = alfabeta(tableroAux,n-1,True,coordenada,aux+1,alfa,beta)
                if resultado != None:
                    resultados.append((resultado[0],coordenada,resultado[2]))
                    if resultado[0] < beta:
                        beta = resultado[0]
                        if alfa >= beta:
                            break
                
                
            if len(resultados) != 0:
                resultado = resultados[0]
                
                for puntos in resultados:
                    if puntos[0] < resultado[0]:
                        resultado = puntos
                    elif puntos[0] == resultado[0] and resultado[2] > puntos[2]:
                            resultado = puntos
                            
                return resultado
            else:
                return None
        
def minimax(tablero,n,turno,coordenada,aux):
    resultados = []
    
    if n == 0 or tablero.cuatroEnRaya() or TableroLleno(tablero):
        posicionesObjetivo = CoordenadasImportantes(tablero)
        return (evalua(tablero,posicionesObjetivo),coordenada,aux)
    else:
        if turno:
            for j in range(tablero.ancho):
                
                i = busca(tablero,j)
                
                if i == -1:
                    continue
            
                tableroAux = Tablero(tablero)
                tableroAux.setCelda(i,j,2)
                
                coordenada = (i,j)
                
                resultado = minimax(tableroAux,n-1,False,coordenada,aux+1)
                resultados.append((resultado[0],coordenada,resultado[2]))
                
            resultado = resultados[0]
            for puntos in resultados:
                if puntos[0] > resultado[0]:
                    if puntos[0] > 80000 and resultado[0] > 80000:
                        if resultado[2] > puntos[2]:
                            resultado = puntos
                    else:
                        resultado = puntos
                elif puntos[0] == resultado[0] and resultado[2] > puntos[2]:
                    resultado = puntos
                elif puntos[0] == resultado[0] and resultado[2] == puntos[2]:
                    aleatorio = random.randint(0, 1)
                    if aleatorio == 0:
                        resultado = puntos
            
            return resultado
        else:
            for j in range(tablero.ancho):
                
                i = busca(tablero,j)
                
                if i == -1:
                    continue
            
                tableroAux = Tablero(tablero)
                tableroAux.setCelda(i,j,1)
                
                coordenada = (i,j)
                
                resultado = minimax(tableroAux,n-1,True,coordenada,aux+1)
                resultados.append((resultado[0],coordenada,resultado[2]))
                
            resultado = resultados[0]
            
            for puntos in resultados:
                if puntos[0] < resultado[0]:
                    resultado = puntos
                elif puntos[0] == resultado[0] and resultado[2] > puntos[2]:
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
        
    puntuacion = 0
            
    for coordenada in coordenadas:
        i = coordenada[0]
        j = coordenada[1]
        
        #"_._._"
        if j < 4:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == 0 and tablero.getCelda(i,j+3) == jugAnalizado and tablero.getCelda(i,j+4) == 0:
                    if SueloFicha(tablero,(i,j+2)) and SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i,j+4)):
                        puntuacion += 1
        #"_
        #"_.
        #"___
        #"___.
        #"_____      
        if j < 4 and i < 3:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j + 1) == jugAnalizado and tablero.getCelda(i + 2,j + 2) == 0 and tablero.getCelda(i + 3,j + 3) == jugAnalizado and tablero.getCelda(i + 4,j + 4) == 0:
                    if SueloFicha(tablero,(i+2,j+2)) and SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i+4,j+4)):
                        puntuacion += 1
                        
        #"     _
        #"    ._
        #"   ___
        #" .____
        #"______
        if j < 5 and i < 3:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j - 1) == jugAnalizado and tablero.getCelda(i + 2,j - 2) == 0 and tablero.getCelda(i + 3,j - 3) == jugAnalizado and tablero.getCelda(i + 4,j - 4) == 0:
                    if SueloFicha(tablero,(i+2,j-2)) and SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i+4,j-4)):
                        puntuacion += 1
             
                        
                        
        #"_.._"
        if j < 5:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == jugAnalizado and tablero.getCelda(i,j+3) == 0:
                    if SueloFicha(tablero,(i,j)) and SueloFicha(tablero,(i,j+3)):
                        puntuacion += 1
            
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
                        puntuacion += 1
                        
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
                        puntuacion += 1
            
    return puntuacion 

def JugadaFinal(tablero,ataque,coordenadas):
    jugAnalizado = 0
    if ataque == True:
        jugAnalizado = 2
    else:
        jugAnalizado = 1
    
    puntuacion = 0
    
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
                        puntuacion +=1
                
            #".
            #"_.
            #"___
            #"___.   
        if j < 5 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j + 1) == jugAnalizado and tablero.getCelda(i + 2,j + 2) == 0 and tablero.getCelda(i + 3,j + 3) == jugAnalizado:
                    if SueloFicha(tablero,(i+2,j+2)):
                        puntuacion +=1
                        
            #"    .
            #"   __
            #" .___
            #".____
        if j > 2 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j - 1) == 0 and tablero.getCelda(i + 2,j - 2) == jugAnalizado and tablero.getCelda(i + 3,j - 3) == jugAnalizado:
                    if SueloFicha(tablero,(i+1,j-1)):
                        puntuacion +=1
                
            #".._."
        if j < 5:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == 0 and tablero.getCelda(i,j+3) == jugAnalizado:
                    if SueloFicha(tablero,(i,j+2)):
                        puntuacion +=1
                
            #".
            #"__
            #"__.
            #"___.   
        if j < 5 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j + 1) == 0 and tablero.getCelda(i + 2,j + 2) == jugAnalizado and tablero.getCelda(i + 3,j + 3) == jugAnalizado:
                    if SueloFicha(tablero,(i+1,j+1)):
                        puntuacion +=1
            #"    .
            #"   ._
            #" ____
            #".____
        if j > 2 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j - 1) == jugAnalizado and tablero.getCelda(i + 2,j - 2) == jugAnalizado and tablero.getCelda(i + 3,j - 3) == jugAnalizado:
                    if SueloFicha(tablero,(i+2,j-2)):
                        puntuacion +=1
                  
            #"..._"
        if j < 5:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == jugAnalizado and tablero.getCelda(i,j+3) == 0:
                    if SueloFicha(tablero,(i,j+3)):
                        puntuacion +=1
                            
            #".
            #"_.
            #"__.
            #"____
        if j < 5 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j + 1) == jugAnalizado and tablero.getCelda(i + 2,j + 2) == jugAnalizado and tablero.getCelda(i + 3,j + 3) == 0:
                    if SueloFicha(tablero,(i+3,j+3)):
                        puntuacion +=1
            #"   _
            #"  ._
            #" .__
            #".___
        if j > 2 and i < 4:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j - 1) == jugAnalizado and tablero.getCelda(i + 2,j - 2) == jugAnalizado and tablero.getCelda(i + 3,j - 3) == jugAnalizado:
                    if SueloFicha(tablero,(i,j)):
                        puntuacion +=1
                
            #"_..."
        if j < 5:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i,j+1) == jugAnalizado and tablero.getCelda(i,j+2) == jugAnalizado and tablero.getCelda(i,j+3) == jugAnalizado:
                    if SueloFicha(tablero,(i,j)):
                        puntuacion +=1
                            
            #"_
            #"_.
            #"__.
            #"___.
        if j < 5 and i < 4:
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i + 1,j + 1) == jugAnalizado and tablero.getCelda(i + 2,j + 2) == jugAnalizado and tablero.getCelda(i + 3,j + 3) == jugAnalizado:
                    if SueloFicha(tablero,(i,j)):
                        puntuacion +=1
            #"    .
            #"   ._
            #" .___
            #"_____
        if j > 2 and i < 4:
            if tablero.getCelda(i,j) == jugAnalizado:
                if tablero.getCelda(i + 1,j - 1) == jugAnalizado and tablero.getCelda(i + 2,j - 2) == jugAnalizado and tablero.getCelda(i + 3,j - 3) == 0:
                    if SueloFicha(tablero,(i+3,j-3)):
                        puntuacion +=1
                            
            #"-
            #". 
            #".
            #".
        if i < 4 :
            if tablero.getCelda(i,j) == 0:
                if tablero.getCelda(i+1,j) == jugAnalizado and tablero.getCelda(i+2,j) == jugAnalizado and tablero.getCelda(i+3,j) == jugAnalizado:
                    if SueloFicha(tablero,(i,j)):
                        puntuacion +=1
                        
    return puntuacion

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