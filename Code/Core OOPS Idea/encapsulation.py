class Library:
    def __init__(self, id, name):
        self.bookId = id
        self.bookName = name
    
    def setBookName(self, newBookName): # setters method to set the book name
        self.bookName = newBookName
    
    def getBookName(self): # getters method to get the book name
        print(f"The name of the book is {self.bookName}")

book = Library(101, "Crack your SQL Interview In One Day")
book.getBookName()
book.setBookName("Crack your Python Django Interview Like a pro")
book.getBookName()
