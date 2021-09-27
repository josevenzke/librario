from rest_framework import serializers
from .models import Book, Review, Author, Tag, BooksRead
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'pages','tags']

class BooksReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    books = BookSerializer(many=True)
    
    class Meta:
        model = BooksRead
        fields= ['user','books']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name', 'age']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'