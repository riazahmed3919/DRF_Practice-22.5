from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, related_name='books')
    published_date = models.DateField()
    availability_status = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title    
