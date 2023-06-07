from turtle import *

speed(0)
def dibujo(size, niveles, angulo):
    if niveles == 0:
        return
    forward(size)
    left(angulo/2)
    dibujo(size*0.8, niveles - 1, angulo)
    backward(size)
    dibujo(size*0.8, niveles - 1, angulo)
    forward(size)
    left(angulo/2)
    dibujo(size*1.1, niveles - 1, angulo)

    for i in range(2):
        backward(size)
        right(10)



if __name__ == "__main__":
    dibujo(20,7,90)
    mainloop()
