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
    posicion = (x,y)
    while posicion != (4,4):
        posicion_nueva = input("¿Hacia donde quiere ir?")
        if posicion_nueva == "s":
            laberinto[x,y] = ' '
            laberinto[x,y+1] = 'o'
            y += 1
        elif posicion_nueva == "a":
            laberinto[x,y] = ' '
            laberinto[x-1,y] = 'o'
            x -= 1
        elif posicion_nueva == "d":
            laberinto[x,y] = ' '
            laberinto[x+1,y] = 'o'
            x += 1
        elif posicion_nueva == "w":
            laberinto[x,y] = ' '
            laberinto[x,y-1] = 'o'
            y -= 1
    print ("¡Ha llegado al final del laberinto, enhorabuena!")

def laberinto():
   crear_laberinto
   movimiento