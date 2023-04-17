admin=["logan", "micropachycephalus232341menlo", "D.DirkHartogs@python.com", "admin"]
user=["adani", "{([])}", "AdaniGautham@ternakuang.com", "apprentice"]
print("welcome to S.Dali's chesterfield.")
print("login required")
while(True):
    login=input("username: ")
    password=input("password: ")
    email=input("email: ")
    if(login==admin[0]):
        if(password==admin[1]):
            if(email==admin[2]):
                print("Welcome, esteemed admin! We are thrilled to have you on board. As the administrator of our platform, you play a vital role in keeping things running smoothly and ensuring that our community thrives. Your expertise, dedication, and leadership are invaluable, and we are grateful for your presence. Thank you for being an essential part of our team, and we look forward to achieving great things together!")
            else:
                print("account does not registered.")
                choice=input("retry (Y/N?) ")
        else:
                print("account does not registered.")
                choice=input("retry (Y/N?) ")
    elif(login==user[0]):            
        if(password==user[1]):
            if(email==user[2]):
                print("Hello and welcome, dear user! We are delighted to have you as a part of our community. Our platform is designed with you in mind, and we are committed to providing you with the best possible experience. Whether you are here to learn, connect, or create, we are here to support you every step of the way. Feel free to explore, engage, and make the most of our resources. Thank you for joining us, and we look forward to sharing an exciting journey together!")
            else:
                print("account does not registered.")
                choice=input("retry (Y/N?) ")
        else:
                print("account does not registered.")
                choice=input("retry (Y/N?) ")
    else:
        print("username does not exist or accident occured. if concern continues, please contact us at m.ziyaibra@gmail.com or at https://www.thisman.org/, or 081454548464.")
        choice=input("retry (y/n?) ")
    if choice=="n":
        break