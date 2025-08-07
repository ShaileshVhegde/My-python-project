import random
computer=random.choice([1,2,3])
youstr=input("enter yor choise")
yourdict={"s":1,"w":2,"g":3}
reversedict={1:"sneak",2:"water",3:"gun"}
you=yourdict[youstr]
print(f"your choise=={reversedict[you]}\ncomputerchoise={reversedict[computer]}")
if(computer == you):
     print("match is draw")
else:
    if(computer==1 and you==2):
        print("computer win")
    elif(computer==1 and you==3):
        print("you win")
    elif(computer==2 and you==1):
        print("you win")
    elif(computer==2 and you==3):
        print("computer win")
    elif(computer==3 and you==1):
        print("computer win")
    elif(computer==3 and you==2):
        print("you win")
    else:
        print("somthing went wrong")