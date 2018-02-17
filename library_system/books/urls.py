from django.urls import path

from books import views

urlpatterns = [
    path('book-list/', views.book_list, name="book-list"),
    path('book-detail/<int:book_id>', views.book_detail, name="book-detail"),
]