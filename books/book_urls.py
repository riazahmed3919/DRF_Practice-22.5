from django.urls import path
from books import views

urlpatterns = [
    path('', views.ViewBooks.as_view(), name='book-list'),
    path('<int:pk>', views.ViewSpecificBooks.as_view(), name='specific-book'),
]
