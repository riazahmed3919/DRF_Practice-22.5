from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, Category, Publisher
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer, PublisherSerializer
from django.db.models import Count

# Create your views here.
@api_view(['GET', 'POST'])
def view_books(request):
    if request.method == 'GET':
        books = Book.objects.select_related('author', 'category', 'publisher').all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_book(request, pk):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
    if request.method == 'PUT':
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        book = get_object_or_404(Book, pk=pk)
        copy_of_book = book
        book.delete()
        serializer = BookSerializer(copy_of_book,context={'request': request})
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def view_categories(request):
    if request.method == 'GET':
        categories = Category.objects.annotate(books_count=Count('books')).all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def view_specific_category(request, pk):
    category = get_object_or_404(Category.objects.annotate(books_count=Count('books')), pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view()
def view_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)

@api_view()
def view_specific_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view()
def view_publishers(request):
    publishers = Publisher.objects.all()
    serializer = PublisherSerializer(publishers, many=True)
    return Response(serializer.data)

@api_view()
def view_specific_publisher(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    serializer = PublisherSerializer(publisher)
    return Response(serializer.data)
