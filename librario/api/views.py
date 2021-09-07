from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Book, Review
from .serializers import BookSerializer,ReviewSerializer


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

@api_view(['GET'])
def listReviewsFromBook(request,book_id):
    reviews = Review.objects.all().filter(book=book_id)
    serialized_reviews = ReviewSerializer(reviews,many=True).data

    return Response({'success':True,'reviews':serialized_reviews})

@api_view(['POST'])
def addReview(request,book_id):
    stars = request.POST.get('stars')
    description = request.POST.get('description')
    recomends = request.POST.get('recomends')

    if not all([stars,description,recomends]):
        return Response({'Success':False})
    
    user = User.objects.get(id=1)
    book = Book.objects.get(id=book_id)

    new_review = Review.objects.create(stars=stars,description=description,recomends=recomends,user=user,book=book)
    serialized_review = ReviewSerializer(new_review).data
    
    return Response({'success':True,'review':serialized_review})