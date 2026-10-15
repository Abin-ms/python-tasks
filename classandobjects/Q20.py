# Q20. Library Management
# Create a class LibraryBook with a constructor that accepts book_name, author, and availability. Create methods to:
# Display book details.
class LibraryBook:
    def __init__(self,book_name,author,is_available):
        self.book_name = book_name
        self.author = author
        self.is_available = is_available
    def display(self):
        print("Book name :",self.book_name)
        print("Author name :",self.author)
        
        print("Is book available :",self.is_available)
l1 = LibraryBook("DVDV","ggg",False)
l1.display()