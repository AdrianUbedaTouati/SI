class Tablero:    
    def __init__(self, tabPadre):
        self.ancho=8
        self.alto=7        
        self.tablero=[]
        #Si no pasa un tablero por parametro, es decir, si tabPadre == null, entonces crea un expande el vector tablero y despues lo rellena con 0, que simboliza un tablero vacio
        if tabPadre==None:
            for i in range(self.alto):           
                self.tablero.append([])
                for j in range(self.ancho):
                    self.tablero[i].append(0)
        else:
            for i in range(self.alto):           
                self.tablero.append([])
                for j in range(self.ancho):
                    self.tablero[i].append(tabPadre.getCelda(i,j))          
        
    def __str__(self):
        salida="  0 1 2 3 4 5 6 7\n"
        for f in range(self.alto):
            salida+=str(f)+" "
            for c in range(self.ancho):         
                if self.tablero[f][c] == 0:
                    salida += ". "
                elif self.tablero[f][c] == 1:
                    salida +="1 "
                elif self.tablero[f][c] == 2:
                    salida += "2 "
                elif self.tablero[f][c] == 3:
                    salida += "3 "
                elif self.tablero[f][c] == 4:
                    salida += "4 "
                elif self.tablero[f][c] == 5:
                    salida += "5 "
                elif self.tablero[f][c] == 6:
                    salida += "6 "
                elif self.tablero[f][c] == 7:
                    salida += "7 "
                elif self.tablero[f][c] == 8:
                    salida += "8 "
                elif self.tablero[f][c] == 9:
                    salida += "9 "
                elif self.tablero[f][c] == 10:
                    salida += "10"
                elif self.tablero[f][c] == 11:
                    salida += "11"
                elif self.tablero[f][c] == 12:
                    salida += "12"
                elif self.tablero[f][c] == 13:
                    salida += "13"
                elif self.tablero[f][c] == 14:
                    salida += "14"
                elif self.tablero[f][c] == 15:
                    salida += "15"
                elif self.tablero[f][c] == 16:
                    salida += "16"
                elif self.tablero[f][c] == 17:
                    salida += "17"
                elif self.tablero[f][c] == 18:
                    salida += "18"
                elif self.tablero[f][c] == 19:
                    salida += "19"
                elif self.tablero[f][c] == 20:
                    salida += "20"
                elif self.tablero[f][c] == 21:
                    salida += "21"
            salida += "\n"
        return salida
        
                
    def getAncho(self):
        return self.ancho
    
    def getAlto(self):
        return self.alto
    
    def getCelda(self, fila, col):
        return self.tablero[fila][col]
    
    def setCelda(self, fila, col, val):
        self.tablero[fila][col]=val    
    
    # detecta si hay cuatro fichas en línea y devuelve el ganador
    def cuatroEnRaya(self):
        i=0        
        fin=False
        ganador=0
        
        while not fin and i<self.getAlto():
            j=0
            while not fin and j<self.getAncho():
                casilla=self.getCelda(i,j)
                if casilla!=0:
                    #búsqueda en horizontal
                    if (j+3) <self.getAncho():
                        if self.getCelda(i, j+1)==casilla and self.getCelda(i, j+2)==casilla and self.getCelda(i, j+3)==casilla:
                            ganador=casilla
                            fin=True
                    #búsqueda en vertical
                    if (i+3) <self.getAlto():
                        if self.getCelda(i+1, j)==casilla and self.getCelda(i+2, j)==casilla and self.getCelda(i+3, j)==casilla:
                            ganador=casilla
                            fin=True
                    #búsqueda en diagonal
                    if (i+3) <self.getAlto():
                        if (j-3) >= 0:
                            if self.getCelda(i+1, j-1)==casilla and self.getCelda(i+2, j-2)==casilla and self.getCelda(i+3, j-3)==casilla:
                                ganador=casilla
                                fin=True
                        if (j+3) <self.getAncho():
                            if self.getCelda(i+1, j+1)==casilla and self.getCelda(i+2, j+2)==casilla and self.getCelda(i+3, j+3)==casilla:
                                ganador=casilla
                                fin=True
                j=j+1
            i=i+1
        return ganador
