# This is coding for functions and docstring

#This is built in function
#a=4
#b=3
#print(sum((a,b)))



#This is user define function

#def number(A,B):
#    mean=(A+B)/2
#    print(mean)
#number(7,8)



def number(A,B):
    """Here we are taking mean value of two element"""
    mean=(A+B)/2
    return(mean)
D=number(7,8)
print(number.__doc__)
print(D)
