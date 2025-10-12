class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    #Adds a Book, EBook, or PrintBook instance to the library.
    def __init__(self, books): 
        #Initializes an empty list to store books in the library.
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)        
    
    def list_books(self): #Prints details of each book in the library.
        return f"{self.book}, {self.book1}, {self.book2}"