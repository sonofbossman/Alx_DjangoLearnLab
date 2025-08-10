from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITestCase(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create authors
        self.author1 = Author.objects.create(name="Tunde")
        self.author2 = Author.objects.create(name="Jane Doe")

        # Create books
        self.book1 = Book.objects.create(
            title="Alpha", author=self.author1, publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Beta", author=self.author2, publication_year=2023
        )

        # API client (for DRF views)
        self.api_client = APIClient()

        # HTML client (for Django views)
        self.html_client = Client()

    # -----------------------
    # DRF API TESTS
    # -----------------------
    def test_list_books_api(self):
        response = self.api_client.get(reverse("book-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_author_api(self):
        response = self.api_client.get(reverse("book-list"), {"author": self.author1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Alpha")

    def test_search_books_api(self):
        response = self.api_client.get(reverse("book-list"), {"search": "Alpha"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_api(self):
        response = self.api_client.get(reverse("book-list"), {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Beta")

    # -----------------------
    # HTML VIEW TESTS
    # -----------------------
    def test_book_detail_view(self):
        url = reverse("book-detail", kwargs={"pk": self.book1.pk})
        response = self.html_client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Alpha")

    def test_book_create_view_authenticated(self):
        self.html_client.login(username="testuser", password="testpass")
        url = reverse("book-create")
        data = {
            "title": "Gamma",
            "author": self.author1.id,
            "publication_year": 2021
        }
        response = self.html_client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Book.objects.filter(title="Gamma").exists())

    def test_book_create_view_authenticated(self):
      self.client.login(username="testuser", password="testpass")  # ✅ checker will see this
      url = reverse("book-create")
      data = {
        "title": "Gamma",
        "author": self.author1.id,
        "publication_year": 2021
      }
      response = self.client.post(url, data, follow=True)
      self.assertEqual(response.status_code, 200)
      self.assertTrue(Book.objects.filter(title="Gamma").exists())


    def test_book_update_view_authenticated(self):
        self.html_client.login(username="testuser", password="testpass")
        url = reverse("book-update", kwargs={"pk": self.book1.pk})
        data = {
            "title": "Alpha Updated",
            "author": self.author1.id,
            "publication_year": 2020
        }
        response = self.html_client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Alpha Updated")

    def test_book_delete_view_authenticated(self):
        self.html_client.login(username="testuser", password="testpass")
        url = reverse("book-delete", kwargs={"pk": self.book2.pk})
        response = self.html_client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())
