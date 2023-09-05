from django.urls import path
from .views import BookListCreateView, add_book_to_reading_list, remove_book_from_reading_list

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:book_id>/add/', add_book_to_reading_list, name='add-book-to-list'),
    path('books/<int:book_id>/remove/', remove_book_from_reading_list, name='remove-book-from-list'),
]
