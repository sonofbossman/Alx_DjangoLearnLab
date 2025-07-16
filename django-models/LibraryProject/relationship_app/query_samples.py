from relationship_app.models import Author, Book, Library, Librarian
# Query all books by a specific author.
author = Author.objects.get(id=2)
books = Book.objects.filter(author=author)
# List all books in a library.
library = Library.objects.get(name="South Brian City Library")
books = library.books.all()
# Retrieve the librarian for a library.
library = Library.objects.get(name="South Brian City Library")
library.librarian