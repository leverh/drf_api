from django.urls import path
from reviews import views

urlpatterns = [
    path('reviews/', views.PostList.as_view()),
    path('reviews/<int:pk>/', views.PostDetail.as_view()),
    path('book-of-the-week/', BookOfTheWeekView.as_view(), name='book-of-the-week'),
]
