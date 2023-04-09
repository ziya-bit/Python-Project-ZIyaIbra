temperature=float(input("input ur room temperature: "))
unit=(input("f/c/k?: "))
outputhbv=(input("General output unit? K/F/C: "))
if unit=="f":
    if outputhbv=="c":
        general_outcome=(temperature-32)/1.8
    elif outputhbv=="k":
        general_outcome=(temperature+459.67)/1.8
    else:
        print ("invalid selectionnaire.")
elif unit=="c":
    if outputhbv=="f":
        general_outcome=(temperature*1.8+32)
    elif outputhbv=="k":
        general_outcome=(temperature+273.15)
    else:
        print ("invalid selectionnaire.")
elif unit=="k":
    if outputhbv=="f":
        general_outcome=(temperature*1.8-459.67)
    elif outputhbv=="c":
        general_outcome=(temperature-273.15)
    else:
        print ("invalid selectionnaire.")
print("ur temper in", outputhbv, "is", general_outcome)