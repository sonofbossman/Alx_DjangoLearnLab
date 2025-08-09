from django.contrib import admin
from .models import Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
  list_display = ['name']

class BookAdmin(admin.ModelAdmin):
  list_display = ['title', 'publication_year', 'author']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)