# This is coding for recursive and iterative approach

# Interative
# def function_1(n):
#     """
#     parameter = integer(n)
#     return = n*n-1*n-2___1
#     """
#     fun=2
#     for j in range(n):
#         fun=fun*(j+1)
#     return fun
# digit=int(input("enter a no.: "))
# print(function_1(digit))




# Recrusive
def funtion_2(n):
    if(n==1):
        return 1
    else:
        return n*funtion_2(n-2)
digit=int(input("enter no.: "))
print(funtion_2(digit))