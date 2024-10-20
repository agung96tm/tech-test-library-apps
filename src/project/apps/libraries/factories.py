import factory
from apps.libraries.models import Author, Book


class AuthorFactory(factory.django.DjangoModelFactory):
    birth_date = factory.Faker("date")
    name = factory.Faker("name")
    bio = factory.Faker("text")

    class Meta:
        model = Author


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("text")
    description = factory.Faker("text")
    author = factory.SubFactory(AuthorFactory)
    publish_date = factory.Faker("date")

    class Meta:
        model = Book
