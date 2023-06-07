from turtle import *

speed(0)
def dibujo(size, niveles, angulo):
    if niveles == 0:
        return
    forward(size)
    left(angulo)
    dibujo(size*0.8, niveles - 1, angulo)
    backward(size)
    dibujo(size*0.8, niveles - 1, angulo)
    forward(size)
    left(angulo)
    dibujo(size*0.8, niveles - 1, angulo)



if __name__ == "__main__":
    dibujo(20,8,90)
    mainloop()
