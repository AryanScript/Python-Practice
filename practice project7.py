# This is coding for making an health managment system
import datetime

B=datetime.datetime.now()

client=int(input("Press 1 for Anni,2 for Maahi,3 for Avni: "))
purpose=int(input("Press 4 for exercise,5 for food: "))

if(client==1):
    if(purpose==4):
        with open("anni_E.txt","a") as F: 
            A=input("exercise performed: ")
            F.write(A+"\t")
            F.write(str(B)+"\n\n")
            print(F)
    elif(purpose==5):
        with open("anni_F.txt","a") as F:
            A=input("food that you have eaten: ")
            F.write(A+"\t")
            F.write(str(B)+"\n\n")
            print(F)
    else:
        print("please choose correct no.")
elif(client==2):
    if(purpose==4):
        with open("maahi_E.txt","a") as F:
            A=input("exercise performed: ")
            F.write(A+"\t")
            F.write(str(B)+"\n\n")
            print(F)
    elif(purpose==5):
        with open("maahi_F.txt","a") as F:
            A=input("food that you have eaten: ")
            F.write(A+"\t")
            F.write(str(B)+"\n\n")
            print(F)
    else:
        print("please choose correct no.")
elif(client==3):
    if(purpose==4):
        with open("avni_E.txt","a") as F:
            A=input("exercise performed: ")
            F.write(A+"\t")
            F.write(str(B)+"\n\n")
            print(F)
    elif(purpose==5):
        with open("avni_F.txt","a") as F:
            A=input("food that you have eaten: ")
            F.write(A+"\t")
            F.write(str(B)+"\n\n")
            print(F)
    else:
        print("please choose correct no.")
else:
    print("please choose correct input")

