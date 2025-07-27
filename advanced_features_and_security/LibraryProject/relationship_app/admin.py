from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile
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

# Register your models here.
admin.site.register([Author, Book, Library, Librarian])
admin.site.register(UserProfile)
admin.site.register(CustomUser, CustomUserAdmin)