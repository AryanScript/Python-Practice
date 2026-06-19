# This is coding for making public, protected, private


class company:
    no_of_leaves=56#(this is public)
    _protec=4
    __private=398
    def __init__(self, rname, remployes, rdate):
        self.name=rname
        self.employe=remployes
        self.establish=rdate
    def details(self):
        return f"The name of company= {self.name}\n\n employe working in company= {self.employe}\n\n establish in= {self.establish}"
    @classmethod
    def change_leaves(cls,new):
        cls.no_of_leaves=new
class new(company):
    def printprog(self):
        return f"The name of company= {self.name}\n\n employe working in company= {self.employe}\n\n establish in= {self.establish}"
company1=company("aryan group of company",456,1984)
company2=company("vansh group of company",500,1999)
company3=new("ayush group of company",567,1988)

d=company("huohdfr",456,678)
print(d._company__private)
