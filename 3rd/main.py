from turtle import *
import turtle
from tkinter import *
from time import sleep
from random import randrange

def main():
    def drawCube(startposition:tuple=(0,0),delaytime=1):

        # register_shape()
        delay(delaytime)
        penup()
        
        def drawSquare(startpos:tuple=(0,0),col="red"):
            """Draws a Square shape

            Args:
                startpos (tuple, optional): Sets shape start position. Defaults to (0,0).
                col (str, optional): Sets shape color. Defaults to "red".
            """
            # colors = ('red', 'blue', 'green', 'orange')
            setpos(startpos)
            pendown()
            color(col)
            goto((startpos[0]+0),(startpos[1]+100))
            goto((startpos[0]-100),(startpos[1]+100))
            goto((startpos[0]-100),(startpos[1]+0))
            goto((startpos[0]+0),(startpos[1]+0))
            penup()
            
        def drawParallelogram(startpos:tuple=(0,0),col="red"):
            """Draws a Parallelogram

            Args:
                startpos (tuple, optional): Sets shape start position. Defaults to (0,0).
                col (str, optional): Sets shape color. Defaults to "red".
            """
            # colors = ('red', 'blue', 'green', 'orange')
            setpos(startpos)
            pendown()
            color(col)
            goto((startpos[0]+50),(startpos[1]+50))
            goto((startpos[0]+50),(startpos[1]+150))
            goto((startpos[0]+0),(startpos[1]+100))
            goto((startpos[0]-0),(startpos[1]+0))
            penup()
            
        drawSquare(((startposition[0]+50),(startposition[1]+50)))
        
        drawParallelogram(((startposition[0]),(startposition[1])))
        drawParallelogram(((startposition[0]-100),(startposition[1]+0)))
        
        drawSquare(((startposition[0]),(startposition[1])))

    pos:tuple = tuple() 
    # randnum = float()
    numx = 0
    numy = int()
    randnum1 = int()
    randnum2 = int()
    for i in range(5):
        # numy += randnum2 
        randnum1 = randrange(-200,201,100)
        numx = randnum1
        
        while numx == randnum1:
            print("esta en la misma posicion", numx, "-",randnum1)
            numx = randrange(-200,201,100)
            print("nueva posicion", numx)
        
        pos = ((numx),(0)) 
        drawCube(pos,0)
    
    def rotateCube():
        coords = tuple(0,0,0)


    input("press ENTER to exit")

if __name__ == '__main__':
    main()


# i = 0
# espacio = "     "
# dibujo = "*"

# while i < 5 :

#     # dibujo = print(" "*o, "#"*i,"\n", end="") # forma 1 de hacerlo, no muy intuitiva
#     # i=i+2

#     print(espacio, dibujo)
#     i=i+1
#     dibujo = dibujo + "**"; # -> ***
#     espacio = espacio.replace(" ","",1); # -> ¨¨¨¨
    

    
