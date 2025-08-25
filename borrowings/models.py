from django.db import models
from books.models import Book
from accounts.models import Member

# Create your models here.
class BorrowRecord(models.Model):
    STATUS_CHOICES = (
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_records')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrow_records')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='borrowed')

    def __str__(self):
        return f"{self.member.first_name} borrowed {self.book.title}, status: {self.status}"
