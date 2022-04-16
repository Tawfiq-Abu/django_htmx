from django.contrib import admin
from .models import Author, Book
'''
this allows us to have book information on the author detail page instead of having
the book detail page on it's own

'''

class BookInLineAdmin(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]


admin.site.register(Author, AuthorAdmin)
