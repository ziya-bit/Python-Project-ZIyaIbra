from turtle import *
def greeting (name):
    print("haegen dazs!.", name)
# greeting("m. jose rizal richard bonifacio")
# greeting("adani")
def ascii (radius, inkfountain="navy", bucketcolor="maroon"):
    fillcolor(bucketcolor)
    begin_fill()
    pencolor (inkfountain)
    circle (radius)
    end_fill()
def caviar (number):
    return number*number