from apps.libraries.mixins import CacheViewMixin
from apps.libraries.models import Author, Book
from apps.libraries.serializers import AuthorSerializer, BookSerializer
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class AuthorListView(CacheViewMixin, ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(CacheViewMixin, RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorBookListView(CacheViewMixin, ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(author__pk=self.kwargs["author_pk"]).all()


class BookListView(CacheViewMixin, ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(CacheViewMixin, RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
