from django.urls import path
from .views import BookListCreateView, add_book_to_reading_list, remove_book_from_reading_list, get_user_reading_list

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('users/<int:user_id>/books/<int:book_id>/add/', add_book_to_reading_list, name='add-book-to-list'),
    path('books/<int:book_id>/remove/', remove_book_from_reading_list, name='remove-book-from-list'),
    path('', get_user_reading_list, name='user-reading-list'),
    path('users/<int:user_id>/books/', get_user_reading_list, name='other-user-reading-list'),
]
