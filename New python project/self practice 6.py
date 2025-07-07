# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

#     def display(self):
#         print(f"Name: {self.name}, Roll: {self.roll}")

# s1 = Student("Abid", 101)
# s2 = Student("Tushar", 102)

# s1.display()
# s2.display()

# class Book:
#     def __init__(self,title,author, year):
#         self.title=title
#         self.author=author
#         self.year=year

#     def showdetails(self):
#         print(f"Name of the book is: {self.title}.Author's name is: {self.author} and year of release is: {self.year}")
    

# b1=Book("Rich Dad, Poor Dad","Robert T Kiosaki", 1995)
# b2=Book("Audacity of Hope","Barak Obama",2015)

# b1.showdetails()
# b2.showdetails()

# class Book:
#     def __init__(title, author):
#         title = "Rich Dad"

# b = Book("Python", "Abid")
# print(b.title)
# class Book:
#     def __init__(self, title):
#         self.title = title

# b = Book("Python")
# print(b.title)
# class Book:
#     def __init__(titlename, authorname): 
#         title = titlename 
#         author = authorname 

# b = Book("Rich Dad", "Robert")
# print(b.title)

# class Book:
#     def __init__(self, title, author, year):
#         self.title=title
#         self.author=author
#         self.release=year
#     def showdetails(self):
#             print(f"Title: {self.title}, Author: {self.author}, Year: {self.release}")
#             if self.release<2000:
#                  print(f"{self.title} is an old book.")
#             else:
#                  print(f"{self.title} is a modern book.")


# b1=Book("Rich dad,poor dad","Robert t kiosaki", 1995)
# b2=Book("Audacity of hope","Barak obama", 2015)

# b1.showdetails()
# b2.showdetails()

class Book:
    def __init__(self,title,author,year):
        # __init__ → Special constructor method, not a regular function. 
        # It means:
        # "When someone types Book(...), this function will run immediately."
#         self → This refers to the object that’s being created
# (e.g., if you're doing b1 = Book(...), then self is b1)
        self.title=title # here, self.title hoitese object er memory.. title hoitese just value which passed in
        self.author=author
        self.year=year
    def showdetails(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

class Library:
    def __init__(self):
        self.books=[]

    def addbooks(self, book):
        self.books.append(book)
    def showallbooks(self):
        print("All books in the Library.")
        for book in self.books:
            book.showdetails()
    def find_old_books(self):
        print("\nOld books(Before 2000)")
        print("-"*30)
        for book in self.books:
            if book.year < 2000:
                book.showdetails()
    def search_book(self):
        a=input("Enter your book's name:").title().lower()
        for bookss in self.books:
            if bookss.title.lower()==a:
                bookss.showdetails()
                print(f"Your book: {bookss.title} has been found")



b1=Book("Rich Dad Poor Dad", "Robert Kiyosaki", 1995)
b2=Book("A Promised Land", "Barak Obama", 2020)
b3=Book("Clean Code", "Robert C. Marin", 1999)
#create library and add books

lib=Library()
lib.addbooks(b1)
lib.addbooks(b2)
lib.addbooks(b3)

lib.showallbooks()

lib.find_old_books()
lib.search_book()