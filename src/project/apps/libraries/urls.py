from django.urls import path

from .views import (
    AuthorBookListView,
    AuthorDetailView,
    AuthorListView,
    BookDetailView,
    BookListView,
)

app_name = "libraries"

urlpatterns = [
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<uuid:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/<uuid:author_pk>/books/", AuthorBookListView.as_view(), name="author-book-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<uuid:pk>/", BookDetailView.as_view(), name="book-detail"),
]
