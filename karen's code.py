# _varstr="!RococoGameboy1800?"
# print(_varstr)
# print(type(_varstr))
# _variente=69
# print(type(_variente))
# _varfloat=69.63892456784567834567823456789012345678923456789
# print(int(_varfloat))
# print(type(_varfloat))
from turtle import *
from time import sleep
penup()
goto(-200, 50)
pendown()
length=int(input("length? "))
height=int(input("height? "))
for i in range(2):
    forward(length)
    right(90)
    forward(height)
    right(90)
print("area=",length*height)
sleep(5)
