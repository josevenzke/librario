from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = 'author'

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to ='books/',blank=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    pages = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    class Meta:
        db_table = 'books'

class BooksRead(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

class Review(models.Model):
    stars = models.IntegerField()
    description = models.CharField(max_length=1000)
    recomends = models.BooleanField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = ForeignKey(Book,on_delete=models.CASCADE)
    class Meta:
        db_table = 'review'
