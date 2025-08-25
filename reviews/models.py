from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from books.models import Book
from accounts.models import Member

# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.first_name} rated {self.book.title} - {self.rating}/5"
