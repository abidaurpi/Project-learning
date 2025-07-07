class Book:
    def __init__(self, title,author, year):
        self.title=title
        self.author=author
        self.__year=year
    
    def showdetails(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.__year}")

    def get_year(self):
        return self.__year
    
    def set_year(self,new_year):
        if 0<new_year<=2025:
            self.__year=new_year
            print("Year updated successfully.")

        else:
            print("Invalid year! Must be between 0 to 2025")

b1=Book("Deep Work", "Cal Newport", 2016)
b1.showdetails()


print("Reading year via getter:", b1.get_year())
b1.__year=2050
print("Directly changed year:",b1.__year)
print("Getter still shows:", b1.get_year())

b1.set_year(2020)
b1.showdetails()

b1.set_year(9999)

