from django.urls import path
from books import views

urlpatterns = [
    path('', views.ViewAuthors.as_view(), name='author-list'),
    path('<int:pk>/', views.ViewSpecificAuthor.as_view(), name='specific-author'),
]
