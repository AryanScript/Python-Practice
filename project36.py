# This is coding for understanding dunder and operater overloding


class company:
    no_of_leaves=56
    def __init__(self, rname, remployes, rdate):
        self.name=rname
        self.employe=remployes
        self.establish=rdate
    def details(self):
        return f"The name of company= {self.name}\n\n employe working in company= {self.employe}\n\n establish in= {self.establish}"
    @classmethod
    def change_leaves(cls,new):
        cls.no_of_leaves=new
    def __add__(self,other):
        return self.establish + other.establish
    def __truediv__(self,other):
        return self.establish / other.establish
    def __repr__(self):
        return f"The company= {self.name}\n\n employe company= {self.employe}\n\n establish in= {self.establish}"
    def __str__(self):
        return f"The name of company= '{self.name}'\n\n employe working in company= '{self.employe}'\n\n establish in= '{self.establish}'"
company1=company("aryan group of company",456,1984)
company2=company("vansh group of company",500,1999)

print(str(company1))