# This is coding for making muliple inheritences


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
class new(company):
    def printprog(self):
        return f"The name of company= {self.name}\n\n employe working in company= {self.employe}\n\n establish in= {self.establish}"
class best:
    def __init__(self,newname,newemploye,newdate):
        self.newname=newname
        self.newemploye=newemploye
        self.newdate=newdate
    def newdetails(self):
        return f"The new name of company= {self.newname}\n\n new employe working in company= {self.newemploye}\n\n new establish in= {self.newdate}"
class the(company,best):
    pass
company1=company("aryan group of company",456,1984)
company2=company("vansh group of company",500,1999)
company3=new("ayush group of company",567,1988)
company4=best("aryan group of company",5677,1900)
company5=the("dftrhi",567,8908)
sd=company5.details()
print(sd)


