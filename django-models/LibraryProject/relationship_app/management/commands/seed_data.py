from django.core.management.base import BaseCommand
from django.db import connection
from faker import Faker
import random

from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
  help = "Seed the database with fake authors, books, libraries and librarians"

  def add_arguments(self, parser):
    parser.add_argument('--authors', type=int, default=5, help="Number of authors to create")
    parser.add_argument('--books', type=int, default=20, help="Number of books to create")
    parser.add_argument('--clear', type=str, default="n", help="Clear existing data")
    parser.add_argument('--libraries', type=int, default=20, help="Number of libraries to create")

  @staticmethod
  def reset_sqlite_sequence(model):
    table_name = model._meta.db_table
    with connection.cursor() as cursor:
      cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}'")
  
  @staticmethod
  def generate_library_name():
    faker = Faker()
    prefixes = ["Central", "Public", "City", "Regional", "Community", "Heritage"]
    suffixes = ["Library", "Book Center", "Reading Room", "Knowledge Hub"]
    return f"{faker.city()} {faker.random_element(prefixes)} {faker.random_element(suffixes)}"

  def handle(self, *args, **options):
    faker = Faker()
    num_authors = options['authors']
    num_books = options['books']
    num_lib = options['libraries']
    clear_existing_data = options['clear']

    # Clear Existing Data (optional)
    if clear_existing_data.lower() == "y":
      self.reset_sqlite_sequence(Author)
      self.reset_sqlite_sequence(Book)
      self.reset_sqlite_sequence(Librarian)
      self.reset_sqlite_sequence(Library)
      self.stdout.write(self.style.NOTICE("Clearing existing data..."))
      Author.objects.all().delete()
      Book.objects.all().delete()
      Library.objects.all().delete()
      Librarian.objects.all().delete()
      self.stdout.write(self.style.NOTICE("Clearing Existing Data Completed Successfully..."))
    
    # Create authors
    self.stdout.write(self.style.NOTICE(f"Creating {num_authors} authors..."))
    authors = [Author(name=faker.name()) for _ in range(num_authors)]
    Author.objects.bulk_create(authors)

    # Create books
    self.stdout.write(self.style.NOTICE(f"Creating {num_books} books..."))
    authors = list(Author.objects.all())
    list_of_books = [Book(title=faker.sentence(nb_words=4), author=random.choice(authors)) for _ in range(num_books)]
    Book.objects.bulk_create(list_of_books)
    
    # Create libraries
    list_of_books = list(Book.objects.all())
    self.stdout.write(self.style.NOTICE(f"Creating {num_lib} libraries..."))
    libraries = Library.objects.bulk_create([Library(name=self.generate_library_name()) for _ in range(num_lib)])
    for library in libraries:
      library.books.set(random.sample(list_of_books, k=random.randint(3,6)))

    # Create Librarians
    self.stdout.write(self.style.NOTICE(f"Creating {num_lib} librarians..."))
    libraries = list(Library.objects.all())
    Librarian.objects.bulk_create([Librarian(name=faker.name(), library=lib) for lib in libraries])
    
    self.stdout.write(self.style.SUCCESS("Seeding complete!"))
