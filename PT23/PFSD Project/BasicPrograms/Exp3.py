class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def display_details(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}")

    def update_details(self, title=None, author=None, isbn=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn
        print("Book details updated successfully.")

    def search(self, query):
        if query.lower() in self.title.lower() or query.lower() in self.author.lower():
            return True
        return False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"Sorry, the book '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")


book1 = Book("The 5 AM Club", "Robin Sharma", "9781443460717")
book2 = Book("1984", "George Orwell", "9780451524935")

book1.display_details()
book2.display_details()

book1.update_details(title="The 5AM Club: Updated Edition")
book1.display_details()

if book1.search("Club"):
    print("Book found!")

book1.borrow()
book1.borrow()
book1.return_book()
book1.borrow()
