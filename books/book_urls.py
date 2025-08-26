from django.urls import path
from books import views

urlpatterns = [
    path('', views.ViewBookList.as_view(), name='book-list'),
    path('<int:pk>', views.ViewBookDetails.as_view(), name='specific-book'),
]
