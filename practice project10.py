# This is coding for making a library


class library:
    def __init__(self,name,list):
        self.booklist=list
        self.name=name
        self.borrow={}

    def books_available(self):
        print(f"The books which are available in library {self.name}")
        for book in self.booklist:
            print(book)

    def book_for_borrow(self,person,book):
        if book not in self.borrow.keys():
            self.borrow.update({book:person})
            print(f"The new book isd updated in library")
        else:
            print(f"The book is not available in library {self.borrow[book]}")
    
    def add_book(self,book):
        self.booklist.append(book)
        print("book has been added to library ")

    def return_book(self,book):
        self.borrow.pop(book)
        

if __name__ == "__main__" :
    AS=library("aryan",["guys","that","this","joe","reacher","finlay","roscoe"])

    while (True):
        print(f"welcome to the {AS.name}. Whats your call choose")
        print("1.display books")
        print("2.borrow books")
        print("3.add books")
        print("4.return books")
    
        user=int(input())
        if user==1:
            AS.books_available()
        elif user==2:
            book=input("which book you want to borrow : ")
            user=input("whats our name : ")
            AS.book_for_borrow(user,book)
        elif user==3:
            book=input("enter book name that you want to add in library : ")
            AS.add_book(book)
        elif user==4:
            book=input("enter book name that you want to return in library : ")
            AS.return_book(book)
        else:
            print("enter valid input")
    
        print("for continue press 'g' and for exit 'n'")
        user_choice=""
        while user_choice!="g" and user_choice!="n":
            user_choice=input()
        if user_choice=="g":
            continue
        elif user_choice=="n":
            exit()