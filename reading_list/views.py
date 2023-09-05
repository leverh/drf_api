from rest_framework import generics
from .models import Book, UserBook
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


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
