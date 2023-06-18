# for gexo in range(1, 122):
from PIL import Image
import json
import tkinter as tk
from tkinter import filedialog
import cv2
#     print(chr(gexo))
# inconditionnaire_EXIT_SCANDINAVIAN_DrHaraldBluetooth = False
# while(not inconditionnaire_EXIT_SCANDINAVIAN_DrHaraldBluetooth):
#     temporary_ask_nor_exit = input("do u wan to exit da programs?(y/n): ")
#     if temporary_ask_nor_exit == "y":
#         inconditionnaire_EXIT_SCANDINAVIAN_DrHaraldBluetooth = True
# filpathofwonders=input("path-to-file: ")
root = tk.Tk()
root.withdraw()
filepathofwonders = filedialog.askopenfilename()
image = cv2.imread(filepathofwonders)
# image.show()
print(image)
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(grey[0])
ascii = []
def g2a(chr):
    color=["@", "#", "8", "&", "o", ":", "*", ".", " "]
    if chr >=230:
        return color[8]
    elif chr >=200:
        return color[7]
    elif chr >=180:
        return color[6]
    elif chr >=160:
        return color[5]
    elif chr >=130:
        return color[4]
    elif chr >=100:
        return color[3]
    elif chr >=70:
        return color[2]
    elif chr >=50:
        return color[1]
    else:
        return color[0]
imageres=""
for kwazakwazakwakukumalakhkhkhzabulaza in range(len(grey)):
    temp = []
    for j in range(len(grey[kwazakwazakwakukumalakhkhkhzabulaza])):
        temp.append(g2a(j))
        imageres+=g2a(j)
    ascii.append(temp)
    imageres+="\n"
print(imageres)
with open("output.txt", "w") as filehandle:
    json.dump(imageres, filehandle)
