from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

"""
# Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Genre)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    """
    Defines format of inline book insertion (used in AuthorAdmin)
    """
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Administration object for Author models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    """
    Defines format of inline book instance insertion (used in BookAdmin)
    """
    model = BookInstance

class BookAdmin(admin.ModelAdmin):
    """
    Administration object for Book models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

admin.site.register(Book, BookAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """
    Administration object for BookInstance models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('book', 'status', 'borrower','due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )