# This is coding for try and execpt


first=input("enter your first no.: ")
second=input("enter your second no.: ")

try:
    print(int(first)+int(second))
except Exception as e:
    print(e)

print("please try after some time")