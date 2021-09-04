from django.test import TestCase
from models import Review, User, Book
# Create your tests here.
class BookTest(TestCase):
    """ Test module for Review model """

    def setUp(self):
        Review.objects.create(stars=5,description="Muito bom",recomends=True,user=User.objects.get(id=1),book=Book.objects.get(id=1))
        Review.objects.create(stars=1,description="Muito ruim",recomends=False,user=User.objects.get(id=1),book=Book.objects.get(id=1))


    def test_review_stars(self):
        review_bom = Review.objects.get(stars=5)
        review_ruim = Review.objects.get(name=1)
        self.assertEqual(
            review_bom, 5)
        self.assertEqual(
            review_ruim, 1)