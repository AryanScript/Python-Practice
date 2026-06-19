## This code is for loop and its practice


#S=("mummy","papa","anni")

#for item in S:
#    print(item)


#concept2
#print("all family member age")
#A=(["mummy:","44"],["papa:","43"],["anni:","12"])

#for item,age in A:
#   print(item,age)


#concept3
#A=(["mummy:","44"],["papa:","43"],["anni:","12"])

#D=dict(A)
#for item,age in D.items():
#    print(item,age)





#practice question

L=("king","queen","joker",1,3,5,7,8,9,344,3,4,6,6664,3699,898,77)

#for item in L:
#    if str(item).isalpha():
#        print(item)




for item in L:
    if str(item).isnumeric() and item>6:
        print(item)
