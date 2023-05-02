print("Make sure you meet all the eligibility requirements to obtain a driver's license in your area.")
while(True):
    name=input("nickname: ")
    gender=input("gender: ")
    email=input("email: ")
    umur=int(input("how's your age: "))
    if (umur<17):
        print("no drivin license for u kids, u guys are terrible at driving. no one belive in you. go home and do ur homeword and never comeback!.")
        break
    elif (umur==17):
        id=int(input("can we have your parents id? else will be disqualified: "))
        print("Welcome to the world of driving! Obtaining your driver's license is an exciting milestone and marks the beginning of a new journey. Driving can be both exhilarating and challenging, but with practice and patience, you will soon become a confident and competent driver. Remember to always prioritize safety, follow traffic rules, and stay aware of your surroundings. With these tips in mind, we wish you the best of luck as you embark on this exciting new adventure.")
    else:
         print("Welcome to the world of driving! Obtaining your driver's license is an exciting milestone and marks the beginning of a new journey. Driving can be both exhilarating and challenging, but with practice and patience, you will soon become a confident and competent driver. Remember to always prioritize safety, follow traffic rules, and stay aware of your surroundings. With these tips in mind, we wish you the best of luck as you embark on this exciting new adventure.")
                

