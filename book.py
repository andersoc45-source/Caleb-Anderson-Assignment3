class Book:
    def __init__(self, title, author, isbn):
        """
        The constructor for Book.

        Args:
            title (string): The title of the book.
            author (string): The author of the book.
            isbn (string): The International Standard Book Number of the book.

        Returns:
            Book: The created book.
        """
        self._title = title
        self._author = author
        self._isbn = isbn

    def __str__(self):
        """
        Assigns a string to book.

        Args:
            None

        Returns:
            string: A formatted string of the Book object.
        """
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}"

    def get_details(self):
        """
        Appends a new book to the provided library list.

        Args:
            None

        Returns:
            dictionary: A dictionary representation of Book. The keys are Title, Author, and ISBN.
        """
        return {"Title": self._title, "Author": self._author, "ISBN": self._isbn}


if __name__ == "__main__":
    # Creating a book object
    my_favorite_book = Book("An Encyclopedia of Tolkien", "David Day", "978-1-64517-009-9")
    print(my_favorite_book)
    print(my_favorite_book.get_details())