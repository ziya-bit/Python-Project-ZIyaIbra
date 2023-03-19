from turtle import *
from time import * 
speed(1)
pencolor("black")
fillcolor("turquoise")
for i in range(4):
    forward(100)
    left(90)
begin_fill()
speed(0)
for i in range(99):
    forward(150)
    left(120)
for i in range(9999):
    forward(1)
    left(360/9999)
end_fill()

sleep(5)