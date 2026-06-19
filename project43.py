# This is coding for making coroutines 


import time
def text_seacher():
    book="You are in my coding page in which I have done many projects"
    time.sleep(3)

    while True:
        text=yield
        if text in book:
            print("This text is present in book")
        else:
            print("This text is not present in book")

search=text_seacher()
next(search)
search.send(input())
search.close()