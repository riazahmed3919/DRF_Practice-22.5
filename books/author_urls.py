from django.urls import path
from books import views

urlpatterns = [
    path('', views.ViewAuthorList.as_view(), name='author-list'),
    path('<int:pk>/', views.ViewAuthorDetails.as_view(), name='specific-author'),
]
