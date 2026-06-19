# This is coding for learning map, filter, reduce

#-----------------MAP-------------------
# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# r=[square,cube]
# for i in range(5):
#     q=list(map(lambda x:x(i),r))
#     print(q)


#----------------filter-----------------
# E=[1,3,5,7,9,11]

# def greater(num):
#     return num>5
# gr=list(filter(greater,E))
# print(gr)


#---------------reduce-------------------
from functools import reduce
B=[1,5,8,6,9,4]
o= reduce(lambda x,y:x*y,B)
print(o)