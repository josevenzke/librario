from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Book, Review
from .serializers import BookSerializer


# Create your views here.
@api_view(['GET'])
def listBook(request):
    books = Book.objects.all()
    serialized_books = BookSerializer(books,many=True).data
    return Response({'success':True,'books':serialized_books})

@api_view(['POST'])
def addBook(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    pages = request.POST.get('pages')
    
    if not all([title,author,pages]):
        return Response({'Success':False})

    new_book = Book.objects.create(title=title,author=author,pages=pages)
    serialized_book = BookSerializer(new_book).data
    return Response({'success':True,'new_book':serialized_book})

@api_view(['POST'])
def addReview(request,id_):
    stars = request.POST.get('stars')
    description = request.POST.get('description')
    recomends = request.POST.get('recomends')

    if not all([stars,description,recomends]):
        return Response({'Success':False})

    return Response({'success':True,'info':[stars,description,recomends,id_]})