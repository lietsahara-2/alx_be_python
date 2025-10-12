class Book:
    #initiated
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    #used __str__ and __repr__ special methods
    # def display_official():<-- this should not be here
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
   
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    #deconstructing
    def __del__(self):
        print(f"Deleting 1984")