#This is coding for making @abstractmethod


from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def shapearea(self):
        return 0
    
class rect(shape):
    def __init__(self):
        self.len=6
        self.bre=8
    def shapearea(self):
        return self.len * self.bre
    
r=rect()
print(r.shapearea())
