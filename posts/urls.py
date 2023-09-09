from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('book-of-the-week/', views.BookOfTheWeekView.as_view(), name='book-of-the-week'),
]
