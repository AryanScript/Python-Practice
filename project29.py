# This is coding for making oops file 


class ticket_holder:
    
    def info(self):
        print(f"\nyour name = {self.name}\nyour age = {self.age}\nfrom = {self.entry}\nto = {self.exit}\nthanks for info we will contact you")
       
s=ticket_holder()


s.name=str(input("ente your name: "))
s.age=str(input("enter your age: "))
s.entry=str(input("from: "))
s.exit=str(input("to: "))
s.info()