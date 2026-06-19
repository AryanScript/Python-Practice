# This is coding for making a game snake, water, gun

import random

print("Welcome to game")
chance=10
human=0
computer=0

while(chance>=1):
    R=str(input("for snake S, for water W, for gun G: "))
    l=["S","W","G"]
    choice=random.choice(l)
    if(R=="S"):
        if R==choice and choice=="S":
            print("match tied\nno points")
        elif choice=="G" and R=="S":
            print("computer won")
            computer+=1
        elif choice=="W" and R=="S":
            print("you won")
            human+=1
        else:
            ("please took correct choice")
    elif(R=="W"):
        if R==choice and choice=="W":
            print("match tied\nno points")
        elif choice=="G" and R=="W":
            print("you won")
            human+=1
        elif choice=="S" and R=="W":
            print("computer won")
            computer+=1
        else:
            ("please took correct choice")
    elif(R=="G"):
        if R==choice and choice=="G":
            print("match tied\nno points")
        elif choice=="S" and R=="G":
            print("you won")
            human+=1
        elif choice=="W" and R=="G":
            print("computer won")
            computer+=1
        else:
            ("please took correct choice")
    else:
        print("game over")
    
    chance=chance-1
    print(chance)

print(f"human points:{human}")
print(f"computer points:{computer}\n\n")      

if(human<computer):
    print("computer won the match")
elif(human>computer):
    print("human won the match")
elif(human==computer):
    print("match draw") 


        
        