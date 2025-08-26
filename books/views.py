from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, Category, Publisher
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer, PublisherSerializer
from django.db.models import Count
from rest_framework.views import APIView

# Create your views here.    
class ViewBooks(APIView):
    def get(self, request):
        books = Book.objects.select_related('author', 'category', 'publisher').all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ViewSpecificBooks(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        copy_of_book = book
        book.delete()
        serializer = BookSerializer(copy_of_book, context={'request': request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class ViewCategories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ViewSpecificCategory(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category.objects.annotate(books_count=Count('books')), pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        copy_of_category = category
        category.delete()
        serializer = CategorySerializer(copy_of_category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class ViewAuthors(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ViewSpecificAuthor(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
    def put(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ViewPublishers(APIView):
    def get(self, request):
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ViewSpecificPublishers(APIView):
    def get(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)
    
    def put(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        serializer = PublisherSerializer(publisher, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
