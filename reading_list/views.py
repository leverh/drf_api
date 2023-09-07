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
def get_reading_list(request):
    user_books = UserBook.objects.filter(user=request.user).select_related('book')
    books = [ub.book for ub in user_books]

    serialized_books = BookSerializer(books, many=True).data

    # Include the is_owner field in the response
    return Response({"results": serialized_books, "is_owner": True})

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_other_user_reading_list(request, user_id):
    target_user = User.objects.get(id=user_id)
    
    user_books = UserBook.objects.filter(user=target_user).select_related('book')
    books = [ub.book for ub in user_books]

    serialized_books = BookSerializer(books, many=True).data

    # Include the is_owner field in the response
    return Response({"results": serialized_books, "is_owner": False})

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_book_to_reading_list(request, book_id, user_id):
    # Check if the currently authenticated user is the owner of the list.
    if request.user.id != user_id:
        return Response({"error": "You don't have permission to add books to this list."}, status=403)

    book = get_object_or_404(Book, id=book_id)
    UserBook.objects.create(user=request.user, book=book)
    return Response({"message": "Book added to reading list!"})

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_book_from_reading_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user_book = UserBook.objects.filter(user=request.user, book=book)

    if not user_book.exists():
        return Response({"error": "You don't have permission to remove this book."}, status=403)

    user_book.delete()
    return Response({"message": "Book removed from reading list!"})