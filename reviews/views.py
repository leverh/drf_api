from rest_framework import status, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewSerializer
from django.http import Http404
from bookhub.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from datetime import timedelta
from django.utils import timezone

# Create your views here.


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.annotate(
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


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')


class BookOfTheWeekView(APIView):

    def get(self, request):
        one_week_ago = timezone.now() - timedelta(days=7)
        recent_reviews = Review.objects.filter(created_at__gte=one_week_ago)
        
        top_review = max(recent_reviews, key=lambda review: review.likes_count + review.comments_count, default=None)
        
        if top_review:
            response_data = {
                'title': top_review.title,
                'author_name': top_review.author_name,
                'content': top_review.content,
                'likes_count': top_review.likes_count,
                'comments_count': top_review.comments_count,
                'image_url': top_review.image.url if top_review.image else None,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "No reviews found in the past week."}, status=status.HTTP_404_NOT_FOUND)