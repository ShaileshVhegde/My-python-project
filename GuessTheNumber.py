import random
n=random.randint(1,100)
a=-1
guess=0
while(a!=n):
    guess+=1
    a=int(input("guess the number  : "))
    if(a>n):
        print("guess the lower number")
    else:
        print("guess the higher number")
print(f"congrts you guess number{a} is currect and you guessed it in {guess} attempt\n thank you")