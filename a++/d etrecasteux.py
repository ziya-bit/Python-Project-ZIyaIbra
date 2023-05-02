from turtle import *
from time import *
from random import *
speed(0)
for i in range(360):
    r=randint(0, 255)
    g=randint(0, 255)
    b=randint(0, 255)
    pencolor((r, g, b))
    forward(100)
    for i in range(3):
        backward(25)
        right(45)
        forward(20)
        backward(20)
        left(90)
        forward(20)
        backward(20)
        right(45)
    backward(25)
    left(1)

sleep(3)
