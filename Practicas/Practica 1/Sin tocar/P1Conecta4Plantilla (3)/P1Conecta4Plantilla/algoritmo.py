
# busca en col la primera celda vacía
def busca(tablero, col):  
    #if tablero.getCelda(0,col) != 0:
    #    i=-1
    i=0
    while i<tablero.getAlto() and tablero.getCelda(i,col)==0:          
        i=i+1      
    i=i-1
   
    return i

# llama al algoritmo que decide la jugada
def juega(tablero, posicion):
    ####################################################
    ## sustituir este código por la llamada al algoritmo
   
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
        
        enc=False
    c=0
    while not enc and c<tablero.getAncho():
        f=busca(tablero, c)
        if f!=-1:
            enc=True
        else:
            c=c+1
            
    c1,f1 = PeligroPartida(tablero)
    
    if c1 != None:
        print("Jugadita peligrosa")
        print(f," f")
        print(c," c")
        
        print(f1," f1")
        print(c1," c1")
        
        posicion[0]=f1
        posicion[1]=c1
    
    elif f!=-1:
        posicion[0]=f
        posicion[1]=c
        
        
    ####################################################  
                