from django.urls import path
from . import views

from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('list-books/', views.listBooks, name='list-books'),
    path('add-book/', views.addBook, name='add-book'),
    path('list-authors/', views.listAuthors, name='list-authors'),
    path('add-author/', views.addAuthor, name='add-author'),
    path('list-reviews/', views.listReviews, name='list-reviews'),
    path('list-book-reviews/<int:book_id>/', views.listReviewsFromBook, name='list-book-reviews'),
    path('add-review/<int:book_id>/', views.addReview, name='add-review'),
    path('list-tags/', views.listTags, name='list-tags'),
    path('add-tag/',views.addTag, name='add-tag'),
    path('list-users/',views.listUsers, name='list-users'),
    path('add-user/', views.addUser, name='add-user'),
    path('add-bookread/', views.addBookRead, name='add-bookread')
]
