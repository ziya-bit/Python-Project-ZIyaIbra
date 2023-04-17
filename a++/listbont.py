GUI = ["guidelines for lisbont", "lexica aperture", 992887, "anaconda"]
print(GUI)
print(GUI[1])
for i in GUI: 
    print(i)
for i in range(len(GUI)):
    print(i)
    print(GUI[i])
GUI[1]="karen"
print(GUI)
newitem="micropachycephalus"
GUI.append(newitem)
print(GUI)
newitems=["adobe firefly", "lightroom", "houdini", "bartega x papermark.id"]
GUI.extend(newitems)
print(GUI)
GUI.insert(3,"windows terminal")
print(GUI)
GUI.remove(992887)
print(GUI)
GUI.pop(3)
print(GUI)
