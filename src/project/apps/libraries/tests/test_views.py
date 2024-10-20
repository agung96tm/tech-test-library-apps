from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.libraries.factories import AuthorFactory, BookFactory
from apps.libraries.models import Author, Book


class TestAuthorListAPIView(APITestCase):
    def test_success_get_list_of_authors(self):
        AuthorFactory.create_batch(5)
        response = self.client.get(reverse("libraries:author-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 5)

    def test_success_create_an_author(self):
        response = self.client.post(reverse("libraries:author-list"), data={
            "name": "the best",
            "bio": "lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "birth_date": "1996-08-08",
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data["id"])
        self.assertTrue(Author.objects.filter(id=response.data["id"]).exists())


class TestAuthorDetailAPIView(APITestCase):
    def test_success_get_author_details(self):
        author = AuthorFactory()
        response = self.client.get(reverse("libraries:author-detail", kwargs={"pk": author.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], str(author.pk))

    def test_success_update_author(self):
        author = AuthorFactory()
        response = self.client.patch(reverse("libraries:author-detail", kwargs={"pk": author.id}), data={
            "name": "another name",
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], str(author.pk))
        self.assertEqual(response.data["name"], "another name")

    def test_success_delete_author(self):
        author = AuthorFactory()
        response = self.client.delete(reverse("libraries:author-detail", kwargs={"pk": author.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Author.objects.filter(id=author.id).exists())


class TestBookListAPIView(APITestCase):
    def test_success_get_list_of_books(self):
        BookFactory.create_batch(5)

        response = self.client.get(reverse("libraries:book-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 5)

    def test_success_create_a_book(self):
        author = AuthorFactory()
        response = self.client.post(reverse("libraries:book-list"), data={
            "title": "the best about my president",
            "author_id": author.id,
            "publish_date": "1996-08-08",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum "
                           "has been the industry's standard dummy text ever since the 1500s",
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data["id"])
        self.assertTrue(Book.objects.filter(id=response.data["id"]).exists())


class TestBookDetailAPIView(APITestCase):
    def test_success_get_book_details(self):
        book = BookFactory()
        response = self.client.get(reverse("libraries:book-detail", kwargs={"pk": book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], str(book.pk))

    def test_success_update_book(self):
        book = BookFactory()
        response = self.client.patch(reverse("libraries:book-detail", kwargs={"pk": book.id}), data={
            "title": "something not right?",
            "publish_date": "1996-08-08",
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], str(book.pk))
        self.assertEqual(response.data["title"], "something not right?")

    def test_success_delete_book(self):
        book = BookFactory()
        response = self.client.delete(reverse("libraries:book-detail", kwargs={"pk": book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book.id).exists())
