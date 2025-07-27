from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
  model = CustomUser
  list_display = ('username', 'email', 'date_of_birth', 'is_staff')
  fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('date_of_birth', 'profile_photo')}),
  )
  add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {'fields': ('date_of_birth', 'profile_photo')}),
  )

class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'publication_year', 'created', 'updated')
  search_fields = ('title', 'author', 'publication_year')
  list_filter = ('author', 'publication_year', 'created', 'updated')

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)