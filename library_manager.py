import book

def add_book(library):
    """
    Appends a new book to the provided library list.

    Args:
        library (list): A list for storing Books.

    Returns:
        None
    """
    print("Enter book information")
    book_title = input("Title: ")
    book_author = input("Author: ")
    book_isbn = input("ISBN: ")

    new_book = book.Book(book_title, book_author, book_isbn)
    library.append(new_book)

def list_books(library):
    """
    Prints the contents of library.
    
    Args:
        library (list): A list for storing Books.
    
    Returns:
        None
    """
    for book in library:
        print(book)

def find_book(library, query):
    """
    Searches library list for a book whose title or author matches the provided query.
    
    Args:
        library (list): A list for storing Books.
        query (string): A keyword used to search for a book
    
    Returns:
        Book: If a book is found.
        None: If no match is found.
    """
    for book in library:
        book_info = book.get_details()
        if book_info.get("Title") == query or book_info.get("Author") == query:
            return book
    return None


my_library = []
# Used to track user input
user_input = '0'

# If user_input equals 4, end the program
while user_input != '4':
    print("1. Add a new book.")
    print("2. List all books.")
    print("3. Find a book.")
    print("4. Exit the program.")
    user_input = input()

    if user_input == '1':
        # Add a new book
        print()
        add_book(my_library)
        print()

    elif user_input == '2':
        # List all books
        print()
        list_books(my_library)
        print()

    elif user_input == '3':
        # Find a book
        print(find_book(my_library, input("Enter a keyword: ")))
        print()