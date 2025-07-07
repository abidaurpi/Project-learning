class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.__author=author
        self.__year=year

    def showdetails(self):
        print(f"Title: {self.title}, Author: {self.__author}, Year: {self.__year}")

    def get_year(self):
        return self.__year
    
    def set_year(self,new_year):
        if 0< new_year <=2025:
            self.__year=new_year
            print("Year updated successfully.")
        else:
            print("Invalid year!! Must be between 1 and 2025")
    def get_author(self):
        return self.__author

    

class Library:
    def __init__(self):
        self.book=[]

    def add_book(self,book):
        self.books.append(book)
        print("Book added to the library.")
    
    def show_all_books(self):
        print("\n All books in Library.")
        for book in self.books:
            book.showdetails()

    def search_book(self, search_title):
        for book in self.books:
            book.showdetails()

    def search_book(self,search_title):
        for book in self.books:
            if book.title.lower()==search_title.lower():
                print("\nBook Found.")
                book.showdetails()
                return book
        print("Book not found.")
        return None
    
    def update_book(self, search_title):
        book=self.search_book(search_title)
        if book:
            new_year=int(input("Enter new year:"))
            book.set_year(new_year)

    def delete_book(self,search_title):
        for i, book in enumerate(self.books):
            if book.title.lower()==search_title.lower():
                del self.books[i]
                print("Book deleted from library.")
                return
        print("Book not found.")            
        

lib=Library()

while True:
    a=int(input("""
            Library Menu:
            1. Add Book
            2. Show All Books
            3. Search Book
            4. Update Book Year
            5. Delete Book
            6. Exit
"""))
    
    if a==1:
        title=input("Enter title:")
        author=input("Enter author:")
        year=input("Enter year:")
        book=Book(title,author,year)
        lib.add_book(book)
        
    elif a==2:
        lib.show_all_books()

    elif a==3:
        title=input("Enter title to search:")
        lib.search_book(title)

    elif a==4:
        title=input("Enter title to update: ")
        lib.update_book(title)

    elif a==5:
        title=input("Enter title to delete:")

    elif a==6:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Try again.")
        