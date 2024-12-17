class Book:
    def __init__(self, name, year,namePublisher,genre,autor,price):
        self.name = name
        self.year = year
        self.namePublisher = namePublisher
        self.genre = genre
        self.autor = autor
        self.price = price

    def inputBook(self):
        self.name = input("Enter book name: ")
        self.year = input("Enter book year: ")
        self.namePublisher = input("Enter book name publisher: ")
        self.genre = input("Enter book genre: ")
        self.autor = input("Enter book author: ")
        self.price = input("Enter book price: ")

    def printBook(self):
        print(f"{self.name}, {self.year}, {self.namePublisher}, {self.genre}, {self.autor}, {self.price}")

    def editBook(self):
        self.name = input("Enter book name: ") or self.name
        self.year = input("Enter book year: ") or self.year
        self.namePublisher = input("Enter book name publisher: ") or self.name
        self.genre = input("Enter book genre: ") or self.genre
        self.autor = input("Enter book author: ") or self.autor
        self.price = input("Enter book price: ") or self.price

book = Book("Name",1992,"NAmePubl","genre","autore",20)
book.printBook()