
from django.urls import path
from . import views
urlpatterns = [
    path('list-books/', views.listBooks, name='list-books'),
    path('add-book/', views.addBook, name='add-book'),
    path('list-authors/', views.listAuthors, name='list-authors'),
    path('add-author/', views.addAuthor, name='add-author'),
    path('list-reviews/', views.listReviews, name='list-reviews'),
    path('list-book-reviews/<int:book_id>/', views.listReviewsFromBook, name='list-book-reviews'),
    path('add-review/<int:book_id>/', views.addReview, name='add-review'),
    path('list-tags/', views.listTags, name='list-tags'),
    path('add-tag/',views.addTag, name='add-tag')
]
