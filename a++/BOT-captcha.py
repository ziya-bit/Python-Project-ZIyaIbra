name1="ziya"
myname="captcha-bot"
name2="general prompt manager"
dataname=""
while(True):
    print("welcome, my name is",myname)
    short_term_stored_user=input("what's your name?: ")
    if short_term_stored_user==name1:
        print("welcome editor!")
        cengneim=input("do u want to change my name? (y/n)")
        if cengneim=="y":
            myname=input("what's my new name?: ")
    elif short_term_stored_user==name2:
        print("welcome editor!")
    elif short_term_stored_user==dataname:
        print("welcome back",dataname)
    else: 
        dataname=short_term_stored_user
        print("Nice to meet u. idk n idc who u are but ur name has been saved to my general data.")
    exit=input("execute program? (y/n): ")
    if(exit=="y"):
        break
    