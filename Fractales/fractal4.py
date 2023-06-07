from turtle import *

speed(0)
def dibujo(size, niveles, angulo):
    if niveles == 0:
        for j in range(3):
            color("red")
            forward(size)
            right(120)
        return
    color("blue")
    forward(size)
    left(angulo/2)
    dibujo(size*0.8, niveles - 1, angulo)
    backward(size/4)
    dibujo(size*0.8, niveles - 1, angulo)
    forward(size)
    left(angulo/2)
    dibujo(size*1.1, niveles - 1, angulo)

    for i in range(4):
        backward(size)
        right(10)



if __name__ == "__main__":
    dibujo(20,5,90)
    mainloop()
