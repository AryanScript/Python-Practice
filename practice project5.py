# This coding is for making a mini game

A=78
N=1
while(N<=5):
    G=int(input("guess the number: "))
    if(G>78):
        print("high")
    elif(G<78):
        print("low")
    else:
        print("you won")
        print(N)
        break
    print("no. of guess left",5-N)
    N=N+1

if(N>5):
    print("game over")