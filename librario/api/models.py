from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    pages = models.IntegerField()
    class Meta:
        db_table = 'books'

class Review(models.Model):
    stars = models.IntegerField()
    description = models.CharField(max_length=1000)
    recomends = models.BooleanField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    book_id = ForeignKey(Book,on_delete=models.CASCADE)
    class Meta:
        db_table = 'review'
