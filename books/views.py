from .models import Author, Book, Category, Publisher
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer, PublisherSerializer
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here. 
class ViewBookList(ListCreateAPIView):
    queryset = Book.objects.select_related('author', 'category', 'publisher').all()
    serializer_class = BookSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class ViewBookDetails(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
  
class ViewCategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 
class ViewCategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(books_count=Count('books'))
    serializer_class = CategorySerializer

class ViewAuthorList(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ViewAuthorDetails(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ViewPublisherList(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class ViewPublisherDetails(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
