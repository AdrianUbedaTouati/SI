import sys, pygame
from tablero import *
from algoritmo import *
from pygame.locals import *

MARGEN=20
ROJO=(255, 0, 0)
AZUL=(0, 0, 255)
AMARILLO=(255, 255, 0)
NEGRO=(0,0,0)
BLANCO=(255, 255, 255)
TAM=60

def main():
    maquina1 = 0
    maquina2 = 0
    CreacionMatriz()
    print(TableroLleno(tableroPrueba))
    
    for i in range(0,16):
        print(f"empieza partida {i}")
        pygame.init()
        
        reloj=pygame.time.Clock()
        screen=pygame.display.set_mode([700, 620])
        pygame.display.set_caption("Practica 1")
        
        game_over=False
        tablero=Tablero(None)
        col=-1
        empieza = True
        while not game_over:
            #for event in pygame.event.get():
                #if event.type==pygame.QUIT:               
                #    game_over=True
                #else:
                        #obtener posición y calcular coordenadas matriciales
                        #juega persona, comprobar casilla y actualizar tablero
                        #pos=pygame.mouse.get_pos()  
                        #colDestino=(pos[0]-(2*MARGEN))//(TAM+MARGEN)
                        #maquina1
                        
                posicion = [-1,-1]
                                        
                if i < 8:
                    if empieza:
                        tablero.setCelda(6,i,1)
                        empieza = False
                    else :
                        juega(tablero, posicion)                
                        tablero.setCelda(posicion[0], posicion[1], 1)
                    print(tablero)
                    if tablero.cuatroEnRaya()==1:
                        game_over=True
                        print ("gana maquina1")
                        maquina1+=1
                    else:  #si la persona no ha ganado, juega la máquina 
                        juega(tablero, posicion)                
                        tablero.setCelda(posicion[0], posicion[1], 2) 
                        print(tablero)
                    if tablero.cuatroEnRaya()==2:
                        game_over=True
                        print ("gana máquina2")
                        maquina2+=1
                else:
                    if empieza:
                        tablero.setCelda(6,i-8,2)
                        empieza = False
                    else :
                        juega(tablero, posicion)                
                        tablero.setCelda(posicion[0], posicion[1], 2)
                    print(tablero)
                    if tablero.cuatroEnRaya()==2:
                        game_over=True
                        print ("gana maquina1")
                        maquina2+=1
                    else:  #si la persona no ha ganado, juega la máquina 
                        juega(tablero, posicion)                
                        tablero.setCelda(posicion[0], posicion[1], 1) 
                        print(tablero)
                    if tablero.cuatroEnRaya()==1:
                        game_over=True
                        print ("gana máquina2")
                        maquina1+=1
                        
                
            #código de dibujo        
            #limpiar pantalla
            #screen.fill(NEGRO)
            #pygame.draw.rect(screen, AZUL, [MARGEN, MARGEN, 660, 580],0)
            #for fil in range(tablero.getAlto()):
            #    for col in range(tablero.getAncho()):
            #        if tablero.getCelda(fil, col)==0: 
            #            pygame.draw.ellipse(screen, BLANCO, [(TAM+MARGEN)*col+2*MARGEN, (TAM+MARGEN)*fil+2*MARGEN, TAM, TAM], 0)
            #        elif tablero.getCelda(fil, col)==1: 
            #            pygame.draw.ellipse(screen, ROJO, [(TAM+MARGEN)*col+2*MARGEN, (TAM+MARGEN)*fil+2*MARGEN, TAM, TAM], 0)
            #        else:
            #            pygame.draw.ellipse(screen, AMARILLO, [(TAM+MARGEN)*col+2*MARGEN, (TAM+MARGEN)*fil+2*MARGEN, TAM, TAM], 0)                
            #                
            #for col in range(tablero.getAncho()):
            #    pygame.draw.rect(screen, BLANCO, [(TAM+MARGEN)*col+2*MARGEN, 10, TAM, 10],0)
                
            #actualizar pantalla
            #pygame.display.flip()
            #reloj.tick(40)
            #if game_over==True: #retardo cuando gana
            #    pygame.time.delay(1500)
        
        #pygame.quit()
    print(f"Maquina 1: {maquina1}| Maquina 2: {maquina2}")
 
if __name__=="__main__":
    main()
 
