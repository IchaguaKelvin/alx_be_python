class Book:
    """Represents a book with a title, author, and availability status."""
    def __init__(self, title, author):
        # Public attributes as requested
        self.title = title
        self.author = author
        self.is_checked_out = False # Attribute to track availability

    def __str__(self):
        """String representation for clean output."""
        return f"{self.title} by {self.author}"

class Library:
    """Manages a collection of Book objects."""
    def __init__(self):
        # Private list to store Book objects
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """Marks a book as checked out (unavailable) by title."""
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out:
                    book.is_checked_out = True
                    print(f"Checked out: {title}")
                    return
                else:
                    print(f"Error: '{title}' is already checked out.")
                    return
        print(f"Error: Book with title '{title}' not found.")

    def return_book(self, title):
        """Marks a book as returned (available) by title."""
        for book in self._books:
            if book.title == title:
                if book.is_checked_out:
                    book.is_checked_out = False
                    print(f"Returned: {title}")
                    return
                else:
                    print(f"Error: '{title}' was not checked out.")
                    return
        print(f"Error: Book with title '{title}' not found.")

    def list_available_books(self):
        """Lists all books that are currently available (not checked out)."""
        available_books = [book for book in self._books if not book.is_checked_out]

        if not available_books:
            print("No books are currently available.")
            return

        for book in available_books:
            print(book)
# library_management.py (ADD THIS CODE INSIDE THE Library CLASS)

    def list_books_by_author(self, author):
        """Lists the titles of all books by a specific author."""
        books_by_author = [book.title for book in self._books if book.author == author]
        
        if books_by_author:
            print(f"Books by {author}:")
            for title in books_by_author:
                print(title)
        else:
            print(f"No books found by author: {author}")

    def delete_book(self, title):
        """Removes a book from the library's collection by title."""
        # Find the book object to remove
        book_to_delete = None
        for book in self._books:
            if book.title == title:
                book_to_delete = book
                break
        
        if book_to_delete:
            self._books.remove(book_to_delete)
            print(f"Deleted: {title}")
        else:
            print(f"Error: Book with title '{title}' not found for deletion.")