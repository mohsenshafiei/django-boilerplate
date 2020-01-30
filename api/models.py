from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    published = models.DateTimeField(blank=True, null=True, default=None)
    cover  = models.ImageField(upload_to='covers/', blank=True)

class Author(models.Model):
    name = models.CharField(max_length=36)
    surname = models.CharField(max_length=36)
    books = models.ManyToManyField(Book, related_name='author')
