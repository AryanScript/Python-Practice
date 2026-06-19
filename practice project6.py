# This is coding for my practice, who's name is astrologer star


A=int(input("enter your no.: "))
B=int(input("choose from 0 and 1: "))
if(B==0):
    print(False)
    for item in range(A,0,-1):
        print("*"*item)
elif(B==1):
    print(True)
    for item in range(1,A+1):
        print("*"*item)
else:
    print("enter 0 and 1 only")
    
    
