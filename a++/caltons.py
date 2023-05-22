print("here's your plce. ur not welcome.")
print("want to convert? nothing to convert here.")
print("1. km/h-m/s i hope u cant do math!")
print("2. m/s-km/h what a failure.")
print("3. km/h-speed of light why u guys are very3 slow?.")
print("4. ")
choice = input("what number did you wanna choose?")
if choice == "1":
    print("km/h-m/s")
    speed = input("how fast can you sprint? ")
    speed = float(speed) 
    print("your speed in m/s = ", speed*10/36)
elif choice =="2":
    print("m/s-km/h")
    speed = input("how fast can you sprint? ")
    speed = float(speed)
    print("your speed in m/s = ", speed*36/10)
elif choice =="3":
    print("the speed of pneumonoultramicroscopicsilicovolcanoconiosis(light) to speed of sound")
    speed = input("how fast can you sprint? ")
    speed = float(speed)
    print("your nasa's speed in light nor electron form = ", speed/1080000000)
else:
    print("what a failure. better ask ur karate sensei!")
