from rest_framework import serializers
from .models import Author, Category, Publisher, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']

class CategorySerializer(serializers.ModelSerializer):
    books_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'books_count']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'published_date', 'availability_status', 'category', 'author', 'publisher']

    author = serializers.HyperlinkedRelatedField(queryset=Author.objects.all(), view_name='author-detail')
    category = serializers.HyperlinkedRelatedField(queryset=Category.objects.all(), view_name='category-detail')
    publisher = serializers.HyperlinkedRelatedField(queryset=Publisher.objects.all(), view_name='publisher-detail')