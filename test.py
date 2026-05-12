from main import Book, User

def test_book_is_available_by_default():
    book = Book("Clean Code", "Robert Martin", 2008, 1)
    assert book.is_available == True

def test_borrowing_makes_book_unavailable():
    book = Book("Clean Code", "Robert Martin", 2008, 1)
    user = User(1, "Alice", 1001)
    user.borrow_book(book)
    assert book.is_available == False

def test_borrower_is_set_correctly():
    book = Book("Clean Code", "Robert Martin", 2008, 1)
    user = User(1, "Alice", 1001)
    user.borrow_book(book)
    assert book.borrower == user


def test_returning_makes_book_available_again():
    book = Book("Clean Code", "Robert Martin", 2008, 1)
    user = User(1, "Alice", 1001)
    user.borrow_book(book)
    user.return_book(book)
    assert book.is_available == True

def test_cannot_borrow_unavailable_book():
    book = Book("Clean Code", "Robert Martin", 2008, 1)
    user1 = User(1, "Alice", 1001)
    user2 = User(2, "Bob", 1002)
    user1.borrow_book(book)
    user2.borrow_book(book)
    assert book.borrower == user1
