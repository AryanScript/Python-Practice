# This is coding for scope, global variable, local variable



# x=34

# def f1(m):
#    global x
#    x=54
#    h=5
#    print(x,h)
#    print(m)
# f1("")




def D():
    x=90
    def S():
        global x
        x=65
    S()
D()
print(x)
