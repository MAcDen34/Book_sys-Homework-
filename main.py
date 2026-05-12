import datetime


class Base:
    def __init__(self,record_id):
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.id = record_id


class Book(Base):
    def __init__(self, title, author, year, record_id):
        super().__init__(record_id)
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
        self.borrower = None

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_available": self.is_available,
            "borrower": self.borrower.name if self.borrower else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class Display:

    @staticmethod
    def display_book_info(book):
        print(f"\nTitle: {book.title}")
        print(f"Author: {book.author}")
        print(f"Year: {book.year}")
        print(f"Available: {'Yes' if book.is_available else 'No'}")
        if not book.is_available:
            print(f"Borrowed by: {book.borrower.name}")

class User(Base):
    def __init__(self,UID,name, record_id):
        super().__init__(record_id)
        self.UID = UID
        self.name = name
        self.borrowed_books = []

    def to_dict(self):
        return {
           "id": self.id,
           "UID": self. UID,
           "name": self.name,
           "borrowed_books_ids":[books.id for books in self.borrowed_books],
           "created_at": self.created_at.isoformat(),
           "updated_at": self.updated_at.isoformat()
        }

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            book.borrower = self
            self.borrowed_books.append(book)
            self.updated_at = datetime.datetime.now()
            book.updated_at = datetime.datetime.now()
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            book.borrower = None
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")


import json

def save_to_json(books, users, filepath = "library_date.json"):
    data = {
        "books": [b.to_dict() for b in books],
        "users": [u.to_dict() for u in users]
    }

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

"Example usage"
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 1)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 2)


book_display = Display()
user1 = User(1,"Alice", 1001)
user2 = User(2,"Bob", 1002)
user3 = User(3, "Collins", 1003)

Display.display_book_info(book1)
user1.borrow_book(book1)

Display.display_book_info(book1)
user2.borrow_book(book1)

user3.borrow_book(book2)

Display.display_book_info(book2)

user3.return_book(book2)



save_to_json(books=[book1, book2], users=[user1, user2, user3])
