from django.urls import path, include

urlpatterns = [
    path('books/', include('books.book_urls')),
    path('categories/', include('books.category_urls')),
    path('authors/', include('books.author_urls')),
    path('publishers/', include('books.publisher_urls')),
]
