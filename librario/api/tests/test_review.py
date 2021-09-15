from django.test import TestCase
from api.models import Review, User, Book
# Create your tests here.
class BookTest(TestCase):
    """ Test module for Review model """

    def setUp(self):
        user = User.objects.create_user(username='test', password='test123')
        book = Book.objects.create(title="Habitos Atomicos",author="James Cordan",pages=400)
        Review.objects.create(stars=5,description="Muito bom",recomends=True,user=user,book=book)
        Review.objects.create(stars=1,description="Muito ruim",recomends=False,user=user,book=book)


    def test_review_stars(self):
        review_bom = Review.objects.get(pk=1).stars
        review_ruim = Review.objects.get(pk=2).stars
        self.assertEqual(
            review_bom, 5)
        self.assertEqual(
            review_ruim, 1)