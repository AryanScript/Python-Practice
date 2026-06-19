# This is coding for making diamond shape problem


class A:
    def the(self):
        print("best class is A")

class B(A):
    def the(self):
        print("best class is ")

class C(A):
    pass

class D(C,B):
    pass

a=A()
b=B()
c=C()
d=D()

d.the()