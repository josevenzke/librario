from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        self.list_book_url = reverse('list-book')
        return super().setUp()

    def tearDown(self):
        return super().tearDown()