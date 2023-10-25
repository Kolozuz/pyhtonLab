import os
import time
from random import randint

# Inizializar tablero (10 x 10) + los borde = (12 x 12)
# Cada posición del tablero son 2 caracteres


def init_maze(rownum):

    default_row =   [" +", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "+ "]
    middle_row =    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "]

    grid =          [["  0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 "]]

    grid.append(default_row)

    i = 0
    while i < rownum:
        grid.append(middle_row + [" "] + [str(i)])
        i += 1

    grid.append(default_row)

    return grid


# Dar valores iniciales a las variables
origen = [1, 0]
grid = init_maze(10)
cantidad_bombas = 10
cantidad_obstaculos = 4

goal_sprite = "\U00002348 "  # "\U000026f3"
imagen_pelota = "o "  # "\U000026aa"
bomb_sprite = "\U00002d5a "  # "\U00012d5a"
imagen_explocion = "\U0001F4A5"  # "\U0001F4A5"
imagen_error = "\U0001F4A5"  # "\U0000274C"
imagen_obstaculo1 = "\\\\"
imagen_obstaculo2 = "//"
# U0001f063 #\U00002348 #1f0df - joker #1f0a0 - black card
origin_sprite = " \U0001f0a0"


def drawGrid():
    #####################################
    # El tablero es una lista recorra las lista imprimiendo los caracteres
    # por filas tablero[fila][columna] las filas y columnas estan en el rango 0 a 12
    os.system("cls")

    for elements in grid:
        row = ''
        for char in elements:
            row += char

        print(row)


def set_startpoint():
    #########################################
    # Origen es una tupla  escriba en ella una ubicación aleatoria (x,0)
    # para ubicar la pelota en la primera columna
    row = randint(2, 11)
    col = int(0)
    grid[row][col] = origin_sprite


def set_goal():
    #############################################################
    # Ubique el blanco en una posición aleatoria de la columna derecha del tablero
    # grid[]
    row = randint(2, 11)
    col = int(11)
    grid[row][col] = goal_sprite

def set_bombs_amount():
    try:
        kk = int(input("How many bombs u want? \n"))
        return kk
    except:
        print("Only integer values allowed")
        exit()

def set_bombs(amount:int):
    #####################################################################
    # ubique en el tablero una aleatoriamente el número de bombas
    # cada bomba se ubica en tablero[x][y] donde x,y son número aleatorios de 1 a 10
    i = int(0)
    while i < amount:
        i +=1
        row = randint(2, 11)
        column = randint(2, 10)
        grid[row][column] = bomb_sprite
   
def set_obstacles():
    pass     
    

def disparar():
    direccion = "derecha"
    estado = "disparando"
    row = origen[0]
    col = origen[1]

    while estado == "disparando":
        #####################################
        # Avanzar la pelola
        # Con la dirección identifique la próxima ubicación del disparo
        #  tip: utilize el elif para izquierda, arriba y abajo
        if direccion == "derecha":
            col = col + 1

        #####################################

        if grid[row][col] == "  ":
            grid[row][col] = imagen_pelota
        elif grid[row][col] == goal_sprite:
            estado = "Felicitaciones!!!!"
        elif grid[row][col] == " |" or grid[row][col] == "| " or grid[row][col] == "--" or grid[row][col] == origin_sprite:
            estado = "Vuelva a internarlo"
            grid[row][col] = imagen_error
        elif grid[row][col] == bomb_sprite:
            pass  # Escriba aquí el código para cuando se encuentra una bomba

        else:  # la posicion es // o \\
            obstaculo = grid[row][col]
            ####################################
            # Add code here to redirect the laser in a different direction (top, right, bottom, left)  when a reflector wall // or \\ is hit.

        time.sleep(0.2)
        drawGrid()
        print(estado)


########################################################
# Inicializa y muestra el tablero oficial
# init_maze()
set_goal()
set_startpoint()

drawGrid()



set_bombs(set_bombs_amount())
drawGrid()

set_obstacles()

disparar()
