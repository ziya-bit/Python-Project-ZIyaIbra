from turtle import *
hideturtle()
import time
inp=input("masukan satu huruf: ")
if inp=="z":
    forward(50)
    right(110)
    forward(100)
    left(110)
    forward(50)
elif inp=="i":
    right(90)
    forward(100)
elif inp=="y":
    right(45)
    forward(50)
    left(90)
    forward(50)
    backward(50)
    right(135)
    forward(60)
elif inp=="a":
    pencolor("blue")
    right(135)
    pencolor("maroon")
    forward(100)
    pencolor("cyan")
    backward(100)
    left(90)
    pencolor("light green")
    forward(100)
    right(145)
    pencolor("yellow")
    forward(120.99999999999999999999999999999999999999999999)
else:
    print(inp, "unaccessable experimental unethical test.")
time.sleep(5)