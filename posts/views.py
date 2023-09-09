from rest_framework import status, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from django.http import Http404
from bookhub.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from datetime import timedelta

# Create your views here.


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'author_name',
        'isbn',
    ]
    search_fields = [
        'owner__username',
        'title',
        'author_name',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')


class BookOfTheWeekView(APIView):

    def get(self, request):
        one_week_ago = timezone.now() - timedelta(days=7)
        recent_post = Post.objects.filter(created_at__gte=one_week_ago).order_by('-created_at').first()

        if recent_post:
            response_data = {
                'title': recent_post.title,
                'author_name': recent_post.author_name
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "No posts found in the past week."}, status=status.HTTP_404_NOT_FOUND)
