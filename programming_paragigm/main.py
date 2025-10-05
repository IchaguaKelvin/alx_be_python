from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    
    # Create Book instances
    brave_new_world = Book("Brave New World", "Aldous Huxley")
    nineteen_eighty_four = Book("1984", "George Orwell")
    
    # Add books to the library
    library.add_book(brave_new_world)
    library.add_book(nineteen_eighty_four)

    # 1. Initial list of available books
    print("1. After Initial Setup:")
    print("Available books after setup:")
    library.list_available_books()
    print("-" * 30)

    # 2. Simulate checking out a book
    print("2. After Checking Out '1984':")
    library.check_out_book("1984") # Check out the book
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()
    print("-" * 30)

    # 3. Simulate returning a book
    print("3. After Returning '1984':")
    library.return_book("1984") # Return the book
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
    
    # 4. Simulate listing books by a specific author
    print("-" * 30)
    print("4. After Listing Books by Author 'George Orwell':")
    library.list_books_by_author("George Orwell")
    print("-" * 30)

    # 5. Simulate deleting a book
    print("5. After Deleting '1984':")
    library.delete_book("1984") # Delete the book
    
    print("\nAvailable books after deleting '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()