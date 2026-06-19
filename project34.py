# This is coding for making super() and Overriding in classes


class A:
    sub=3
    def __init__(self):
        self.h="good"
        self.g="perfect"
        self.special="incredibal"
class B(A):
    def __init__(self):
        super().__init__()
        self.h="good"
        self.g="perfect"
  
a=A()
b=B()
print(b.special)

    