from django.urls import path
from reviews import views

urlpatterns = [
    path('reviews/', views.PostList.as_view()),
    path('reviews/<int:pk>/', views.PostDetail.as_view())
]
