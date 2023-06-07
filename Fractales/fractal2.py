from turtle import *
import multiprocessing as mp

speed(0)
def dibujo(size, niveles, angulo):
    if niveles == 0:
        return
    forward(size)
    left(angulo)
    dibujo(size*0.8, niveles - 1, angulo)
    backward(size/2)
    dibujo(size*0.8, niveles - 1, angulo)



if __name__ == "__main__":
    # p1 = mp.Process(target=dibujo, args=(50,10,90))
    # p1.start()
    dibujo(50,10,90)
    dibujo(50,10,90)
    dibujo(50,10,90)
    dibujo(50,10,90)
    mainloop()
