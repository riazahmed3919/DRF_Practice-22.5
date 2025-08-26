from .models import Author, Book, Category, Publisher
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer, PublisherSerializer
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('author', 'category', 'publisher').all()
    serializer_class = BookSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(books_count=Count('books')).all()
    serializer_class = CategorySerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer