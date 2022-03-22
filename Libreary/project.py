class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def dispalyAvailableBooks(self):
        print("The books present in the library are: ")
        for book in self.books:
            print(" *", book)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}.Please Keep it safe and return the book within 30 days ")
            self.books.remove(bookName)
        else:
            print("Sorry...This book has either already been issued to someone else or not avalilable. Please wait until the book is available")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it ! Have a great day ahead")


class Student:
    def requestBook(self):
        self.book = input("Enter the book name youe want to borrow : ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the book name youe want to return : ")
        return self.book


if __name__ == "__main__":
    centerLibrary = Library(
        ["Algorithm", "python", "DBMS", "Operating System", "AI&ML"])
    # centerLibrary.dispalyAvailableBooks()
    student = Student()
    while(True):
        welcome = '''\n***** WELCOME TO CENTRAL LIBRABY*****
         Please choose an option
         1.List the books
         2.Request a book
         3.Return a book
         4.Exit the libraby'''
        print(welcome)
        a = int(input("Enter your option : "))
        if a == 1:
            centerLibrary.dispalyAvailableBooks()
        elif a == 2:
            centerLibrary.borrowBooks(student.requestBook())
        elif a == 3:
            centerLibrary.borrowBooks(student.returnBook())
        elif a == 4:
            print("Thanks for coming to cental library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choose")
