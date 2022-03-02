from datetime import datetime

class Library :
    """wait until program is ready"""
    def __init__(self,list_of_books,name_library):
        self.list_of_books = list_of_books
        self.name_library = name_library

    def display_books(self):
        print(f"\nWe have these books available : ")
        for book in self.list_of_books :
            print(book)

    def lend(self):
        name = input("Enter your name for lending book : ")
        book = input("Enter the name of the which you want to lend : ")
        time = datetime.now().strftime("%d-%m-%y at %H:%M")
        if book in self.list_of_books :
            print(f"Ok,You can lend {book} book\n")
            with open("log_of _library.txt", "a") as lol:
                lol.write(f"{name} lend this book at {time}\n")
            self.list_of_books.remove(book)
        else :
            print("We don't have this book (plz check the list of books which are avaiable\n)")

    def add(self):
        book_name = input("Enter the name of the which you want to add :")
        time = datetime.now().strftime("%d-%m-%y at %H:%M")
        self.list_of_books.append(book_name)
        with open("log_of _library.txt","a") as lol :
            lol.write(f"{book_name} add in our library at {time}\n")
        print(f"\n{book_name} is sucessfully added to library\n")

    def return_book(self):
        book = input("Enter the name of book which you want to return back : ")
        self.list_of_books.append(book)
        time = datetime.now().strftime("%d-%m-%y at %H:%M")
        with open("log_of _library.txt","a") as lol :
            lol.write(f"{book} is return back to library at {time}\n")
        print(f"\n{book} is sucessfully return to library\n")

while True :
    choice = int(input("Enter your choice \n'1' for Create a new library\n'2' for display books name"
                       "\n'3' for lend book\n'4' for add book\n'5' for return book\n'6' for log of library"
                       "\n'7' for exit "))
    if choice == 1 :
        l = []
        name_library = input("Enter the name of your library like this suraj_library : ")
        n = int(input("Enter how many books you wanna add : "))
        for i in range(n) :
            add = input(f"Enter name of book no.{i + 1} : ")
            l.append(add)
        library = Library(l,name_library)

    elif choice == 2 :
        library.display_books()
        print()
    elif choice == 3 :
        library.lend()
    elif choice == 4 :
        library.add()
    elif choice == 5 :
        library.return_book()
    elif choice == 7 :
        break
    elif choice == 6 :
        with open("log_of _library.txt","rt") as lol :
            print(lol.readlines())
