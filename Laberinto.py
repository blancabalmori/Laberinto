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

filas = 5 
columnas = 5

x = 0
y = 0

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
    print (laberinto)

def movimiento(x,y):
    posición = (x,y)
    posicion_nueva = input("¿Hacia donde quiere ir?") 
    if posicion_nueva == "s":
        y += 1
    elif posicion_nueva == "a":
        x -= 1
    elif posicion_nueva == "d":
        x += 1
    elif posicion_nueva == "w":
        y -= 1

def laberinto():
   crear_laberinto
   movimiento