from django.contrib import admin
from books.models import Book, Author

class BookInline(admin.StackedInline):
  '''
  Book inline for AuthorAdmin
  '''
  model = Book
  extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  '''
  Model admin for Author model
  '''
  inlines = [BookInline]
  search_fields = ['first_name', 'last_name']
  list_filter = ['nationality']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  '''
  Model admin for Book model.
  '''
  
  list_display = ['title', 'publication_date', 'created', 'modified']
  search_fields = ['title']
  list_filter = ['publication_date', 'modified']
  raw_id_fields = ['author']
