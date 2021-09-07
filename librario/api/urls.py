
from django.urls import path
from . import views
urlpatterns = [
    path('list-books/', views.listBooks,name='list-books'),
    path('add-book/',views.addBook,name='add-book'),
    path('list-book-reviews/<int:book_id>/',views.listReviewsFromBook,name='list-book-reviews'),
    path('add-review/<int:book_id>/',views.addReview,name='add-review')
]
