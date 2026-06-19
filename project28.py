#This is coding for class and object(oops)


# class company:
#     pass

# company1=company()
# company2=company()
# r=int(input("choose company 1 or 2: "))
# if(r==1):
#     y=company1.name="aryan groups of company\n"
#     j=company1.employe="employe = 600\n"
#     u=company1.establish=1984
#     print(y,j,u)
# if(r==2):
#     g=company2.name="vansh groups of company\n"
#     k=company2.employe="employe = 700\n"
#     s=company2.establish=1989
#     print(g,k,s)
# else:
#     print("we have only two company")



# There is second method to do this 


# class company:
#     def details(self):
#         return f"The name of company= {self.name}\n\n employe working in company= {self.employes}\n\n establish in= {self.date}"
    
# company1=company()
# company2=company()

# company1.name="aryan group of company"
# company1.employes=678
# company1.date=1967

# company2.name="vansh group of company"
# company2.employes=789
# company2.date=1969

# r=int(input("choose company 1 or 2: "))
# if(r==1):
#     print(company1.details())
# elif(r==2):
#     print(company2.details())
# else:
#     print("we have only two company")






class company:
    def __init__(self, rname, remployes, rdate):
        self.name=rname
        self.employe=remployes
        self.establish=rdate
    
    def details(self):
        return (f"The name of company= {self.name}\n\n employe working in company= {self.employe}\n\n establish in= {self.establish}")

   
company1=company("aryan group of company",456,1984)
company2=company("vansh group of company",500,1999)

print(company1.details())