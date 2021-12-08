import math

cell = ' '
wall = 'x'
ficha = 'o'

muro = (
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    (1,1),
    (2,1),
    (2,3),
    (3,3),
    (4,0),
    (4,1),
    (4,2),
    (4,3)
)
empezar = (0,0)
acabar = (4,4)

filas = 5 
columnas = 5

def crear_laberinto (filas, columnas):
    laberinto = []
    for i in range (filas):
        linea = []
        for j in range (columnas):
            if muro:
                linea.append(wall)
            elif (0,0):
                linea.append(ficha)
            else:
                linea.append(cell)

def movimiento():
    posición = (0,0)
    posicion_nueva = input("¿Hacia donde quiere ir?") 
    if posicion_nueva == "s" :
        posición = 



def laberinto():
   
    crear_laberinto