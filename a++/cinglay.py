import random
numpad=[]
for i in range(100):
    numpad.append(random.randint(0, 99999999999999999999999999999999999999999999999))
print(numpad)
kapungkap_genaap=[]
kloaka_ganjeel=[]
for i in numpad:
    if i % 2 == 0:
        kapungkap_genaap.append(i)
    else:
        kloaka_ganjeel.append(i)
        
print(kapungkap_genaap)
print(kloaka_ganjeel)