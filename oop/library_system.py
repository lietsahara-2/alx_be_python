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
    def __init__(self): 
        #Initializes an empty list to store books in the library.
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)   

    def __str__(self):
        return f"{self.book}, {self.book1}, {self.book2}"     
    
    def list_books(self):
        for book in self.books:
            print(
            f"{book.__class__.__name__}: {book.title} by {book.author}"
            f"{', File Size: ' + str(book.file_size) + 'KB' if isinstance(book, EBook) else ''}"
            f"{', Page Count: ' + str(book.page_count) if isinstance(book, PrintBook) else ''}"
        )