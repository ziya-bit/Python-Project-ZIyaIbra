from turtle import *
from time import *
speed(0)
for i in range(360):
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
