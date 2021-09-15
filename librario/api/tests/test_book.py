from django.test import TestCase
from api.models import Book
# Create your tests here.
class BookTest(TestCase):
    """ Test module for Book model """

    def setUp(self):
        Book.objects.create(title="Habitos Atomicos",author="James Cordan",pages=400)
        Book.objects.create(title="Assembly",author="Ygor Narkog",pages=465)

    def test_book_author(self):
        book_habitos = Book.objects.get(name='Habitos Atomicos')
        book_assembly = Book.objects.get(name='Assembly')
        self.assertEqual(
            book_habitos.author, "James Cordan")
        self.assertEqual(
            book_assembly.author, "Ygor Narkog")