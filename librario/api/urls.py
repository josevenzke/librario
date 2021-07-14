
from django.urls import path
from . import views
urlpatterns = [
    path('list-book/', views.listBook),
    path('add-book/',views.addBook),
    path('add-review/',views.addReview)
]
