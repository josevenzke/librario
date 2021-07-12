from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


# Create your views here.
@api_view(['GET'])
def listBook(request):
    books = Book.objects.all()
    serialized_books = BookSerializer(books,many=True)
    return Response({'Books':serialized_books.data})

@api_view(['POST'])
def addBook(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    pages = request.POST.get('pages')
    
    if not all([title,author,pages]):
        return Response({'Success':False})

    new_book = Book.objects.create(title=title,author=author,pages=pages)

    return Response({'Success':True})