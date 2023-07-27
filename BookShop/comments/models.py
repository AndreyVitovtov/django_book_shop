from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from app.models import Book


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    is_member = models.BooleanField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment on '{self.book.title}'"