# This is coding for making setters and property decorater


class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        

    def d(self):
        return f"your first name {self.fname} and your last name {self.lname}"
    @property
    def eemail(self):
        return f"{self.fname}.{self.lname}@gmail.com"
        
a=person("aryan","singh")
b=person("ayush","srivastav")
c=person("vansh","dadhich")
d=person("anuj","dassa")    
d.fname="jay"
d.lname="soni"
print(d.eemail)
    