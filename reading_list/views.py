from rest_framework import generics, permissions, status
from .models import Book, UserBook
from .serializers import BookSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_reading_list(request):
    # Fetch the UserBook objects for the logged-in user
    user_books = UserBook.objects.filter(user=request.user)

    # Extract the associated Book objects
    books = [user_book.book for user_book in user_books]

    # Serialize the books
    serialized_books = BookSerializer(books, many=True)

    return Response(serialized_books.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_book_to_reading_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    UserBook.objects.create(user=request.user, book=book)
    return Response({"message": "Book added to reading list!"})


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_book_from_reading_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    UserBook.objects.filter(user=request.user, book=book).delete()
    return Response({"message": "Book removed from reading list!"})
