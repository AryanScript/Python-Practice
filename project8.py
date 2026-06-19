# This project is based on dictionary and its function 


D1={"aryan":"pachwas","vansh":"makrana","anuj":"khandela"}
#print(D1)



# In this code,adding and deleting the element
#D1.update({"ayush":"banaras"})
#print(D1)

#del D1["anuj"]
#print(D1)



# In this code,functions of dictionary 
#print(D1.items())
#print(D1.keys())
#print(D1.get("vansh"))



# In this code, giving referel to two dictionary
D2=D1
del D2["anuj"]
print(D2)