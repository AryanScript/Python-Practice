#This is coding for dcorator


def reg(hunt1):
    def great():
        print("not interested")
        hunt1()
        print("now interested")
    return great()

@reg
def hunt2():
    print("aryan is caring")