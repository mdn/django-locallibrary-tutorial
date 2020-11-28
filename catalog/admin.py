from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

"""Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Genre)
admin.site.register(Language)


class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('memorizable_week_target', 'created_datetime')
    fields = ['memorizable_week_target', ('created_datetime', 'updated_datetime')]
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('created_datetime', 'author', 'plan_duration_mins', 'due_datetime', 'filepath_for_readiness_enhancement', 'hyperlink_for_readiness_enhancement', 'associated_email_subject', 'associated_email_received_datetime', 'associated_email_received_account', 'filepath_for_readiness_enhancement')
    inlines = [BooksInstanceInline]


admin.site.register(Book, BookAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Administration object for BookInstance models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('book', 'created_datetime', 'updated_datetime', 'target_group_question', 'memorizable_workpackage_relevantinformation_tobememorized', 'relevantinformation_comment', 'is_workpackage', 'memorization_sequence', 'memorization_sequence_is_fixed_because_memorized', 't_information_item_tobeoperationalized_id', 't_memory_palace_type_location_number_id', 'id_asinteger', 't_memorization_package_memory_palace_or_cards_technique_fk2_id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'target_group_question', 'memorizable_workpackage_relevantinformation_tobememorized', 'relevantinformation_comment', 'is_workpackage', 'memorization_sequence', 'memorization_sequence_is_fixed_because_memorized')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
