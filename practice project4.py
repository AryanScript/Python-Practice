# This coding is for making a faulty calculater


A=int(input("enter your 1 no.: "))
B=int(input("\nenter your 2 no.: "))
C=input("\nenter your operation: ")

if(C=="+"):
   if(A==6 and B==7):
      print("\n26")
   else:
      print("\n",A+B)
elif(C=="-"):
   if(A==5 and B==3):
      print("\n45")
   else:
      print("\n",A-B)
elif(C=="*"):
   if(A==2 and B==4):
      print("\n7")
   elif(A==4 and B==2):
      print("\n7")
   else:
      print("\n",A*B)
elif(C=="%"):
   if(A==9 and B==1):
      print("\n5")
   else:
      print("\n",A%B)
elif(C=="/"):
   if(A==3 and B==9):
      print("\n6")
   else:
      print("\n",A/B)
else:
   print("\nenter correct operater")


   