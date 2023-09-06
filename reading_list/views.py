from rest_framework import generics
from .models import Book, UserBook
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        print(f"User ID: {user.id}")

        user_books = UserBook.objects.filter(user=user)
        print(f"UserBooks: {user_books}")

        book_ids = [user_book.book.id for user_book in user_books]
        print(f"Book IDs: {book_ids}")

        return Book.objects.filter(id__in=book_ids)



@api_view(['POST'])
def add_book_to_reading_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    UserBook.objects.create(user=request.user, book=book)
    return Response({"message": "Book added to reading list!"})


@api_view(['DELETE'])
def remove_book_from_reading_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    UserBook.objects.filter(user=request.user, book=book).delete()
    return Response({"message": "Book removed from reading list!"})
