import math

celda = ' '
muro = 'x'

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

def crear_laberinto ():
    laberinto = []