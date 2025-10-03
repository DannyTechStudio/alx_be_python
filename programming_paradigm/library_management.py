
class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def checked_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
        

class Library:
    
    def __init__(self):
        self._books = []
        
    def add_book(self, book):
        self._books.append(book)
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                return book.checked_out()
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False
    
    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"    " + book.title +  " by " + book.author)
        return self._books
        
        

































"""
CLASS Book:
    PUBLIC ATTRIBUTE: title
    PUBLIC ATTRIBUTE: author
    PRIVATE ATTRIBUTE: _is_checked_out (default False)

    METHOD __init__(self, title, author):
        SET self.title = title
        SET self.author = author
        SET self._is_checked_out = False

    METHOD check_out(self):
        IF self._is_checked_out is False:
            SET self._is_checked_out = True
            RETURN True   # successfully checked out
        ELSE:
            RETURN False  # already checked out

    METHOD return_book(self):
        IF self._is_checked_out is True:
            SET self._is_checked_out = False
            RETURN True   # successfully returned
        ELSE:
            RETURN False  # wasn't checked out

    METHOD is_available(self):
        RETURN NOT self._is_checked_out


CLASS Library:
    PRIVATE ATTRIBUTE: _books (list of Book objects)

    METHOD __init__(self):
        SET self._books = empty list

    METHOD add_book(self, book):
        APPEND book to self._books

    METHOD check_out_book(self, title):
        FOR each book in self._books:
            IF book.title == title:
                RETURN book.check_out()
        RETURN False  # book not found

    METHOD return_book(self, title):
        FOR each book in self._books:
            IF book.title == title:
                RETURN book.return_book()
        RETURN False  # book not found

    METHOD list_available_books(self):
        FOR each book in self._books:
            IF book.is_available() is True:
                PRINT "   " + book.title + " by " + book.author

"""























