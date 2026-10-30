import random
Cash=0
while True:
    user_input=input("Would you like to enter a coin?").lower()
    if user_input=="yes":
        Cash-=1
        apple=[random.randint(1,7), random.randint(1,7), random.randint(1,7)]
        print(apple)
    elif [0]==[1] and [1]==[2]:
        print("Jackpot! +10 cash")
        Cash+=10
    elif [0]==7 and [1]==7 and [2]==7:
        print("*$([~777~])$* +100 cash")
        Cash+=100
    user_input=input("Would you like to see you current cash?").lower()
    if user_input=="yes":
        if Cash<-100:
            print("You are in debt "f"{Cash} cash, I feel bad for you.")
        elif Cash<-25:
            print("You are in debt "f"{Cash} cash geez, someone didn't get lucky")
        elif Cash<0:
            print("You are in debt "f"{Cash} cash.")
        elif Cash>0:
            print("Damn bro you only got "f"{Cash} cash? YOUR BROKE ROFL XD")
        elif Cash>25:
            print("You got "f"{Cash} cash? Your pretty lucky.")
        elif Cash>100:
            print("YOU GOT "f"{Cash} CASH? YOU ARE RICH!")
        elif Cash>250:
            print("You have "f"{Cash} cash? Are you Bill Gates perchance?")
        elif Cash>500:
            print("HOW DO YOU HAVE "f"{Cash} CASH? HOLY HAX")
        elif Cash>1000:
            print("YOU HAVE "f"{Cash} CASH? LEAVE SOME FOR THE REST OF US")
        elif Cash>5000:
            print("YOU ARE CHEATING BECAUSE HOW DO YOU HAVE "f"{Cash} CASH?")
