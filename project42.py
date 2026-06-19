# This is coding for learning try except and else both


try:
    f=open("as.txt")

except Exception as e:
    print(e)

else:
    print("Yes this will work when except will not work")

finally:
    print("this will work definetly")
    print("either try except and else will work or not")
    f.close()

print("It's done")