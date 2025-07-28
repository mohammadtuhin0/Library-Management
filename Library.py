class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"The Book '{book_name}' has been added to the library.")
        
    def show_books(self):
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("There are no books in the library.")
    
    def issus_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"The book '{book_name}' has been issued.")
        else:
            print(f"The book is not available in the library.")
lib = Library()
lib.add_book("Python Programming")
lib.add_book("Machine Learning")
lib.add_book("C Programming")
lib.show_books()
lib.issus_book("Python Programming")
lib.show_books()