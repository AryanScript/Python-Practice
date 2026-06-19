# This is coding for pickel module


import pickle

# car=["Dzire","dodge","nissan gtr","camero gt", "scorpio"]
# file="car.col"
# fileobj= open(file,"wb")
# pickle.dump(car,fileobj)
# fileobj.close()


file="car.col"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)