
from django.urls import path
from . import views
urlpatterns = [
    path('list-book/', views.listBook,name='list-book'),
    path('add-book/',views.addBook,name='add-book'),
    path('list-review/<int:book_id>/',views.listReviewsFromBook,name='list-review'),
    path('add-review/<int:book_id>/',views.addReview,name='add-review')
]
