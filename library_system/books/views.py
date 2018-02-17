from books.models import Book
from django.http import HttpResponse
from django.shortcuts import render


def book_list(request):
    """
    List books.
    """
    print('>>>')
    print(request.GET)
    books = Book.objects.all().prefetch_related('author')
    context = {
        'books': books,
    }
    return render(request, 'book_list.html', context)


def book_detail(request, book_id):
    """
    Book detail.
    """
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context)

