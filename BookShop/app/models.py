from django.db import models
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title


class Book(models.Model):
    title = models.TextField(max_length=200)
    img = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    price = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, default='')

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self) -> str:
        return self.title
